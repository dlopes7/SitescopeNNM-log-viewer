import json
import os


def del_dups(seq):
    seen = {}
    pos = 0
    for item in seq:
        if item not in seen:
            seen[item] = True
            seq[pos] = item
            pos += 1
    del seq[pos:]
    return seq

def popula_alertas(sitescope):
    dic_alertas = []
    num_alertas = 0

    estrutura = ['comando', 'emails', 'objeto', 'familia', 'node', 'hora', 'severidade', 'nome']
    captura_data = False

    arquivos = os.listdir(sitescope)
    for arquivo in arquivos:
        try:
            alertas = open(sitescope + '/' + arquivo, 'r', encoding="utf-8")
            linhas = alertas.readlines()
        except UnicodeDecodeError:
            alertas = open(sitescope + '/' + arquivo, 'r', encoding="latin-1")
            linhas = alertas.readlines()


        for linha in reversed(linhas):
            linha = (linha.rstrip('\n'))
            #se a linha comeca com 'Command:'
            if(linha[:8]) == 'Command:':
                parametros =  list(parametro.replace('\"', '') for parametro in linha.split('" '))
                if len(parametros) == 8:
                    num_alertas +=1
                    captura_data = True
                    #print(parametros)
                    #for i in range(len(parametros)):
                    #print (estrutura[i], '\t', parametros[i]

                    #Thu Jul 09 15:47:13 BRT 2015
                    hora = parametros[5][:-9]


                    dic_alertas.append({
                        'ID': num_alertas,
                        estrutura[0]: parametros[0].replace('Command: ', '').replace('com.hp.nms.incident.family.', ''),
                        estrutura[1]: parametros[1].replace('Command: ', '').replace('com.hp.nms.incident.family.', ''),
                        estrutura[2]: parametros[2].replace('Command: ', '').replace('com.hp.nms.incident.family.', ''),
                        estrutura[3]: parametros[3].replace('Command: ', '').replace('com.hp.nms.incident.family.', ''),
                        estrutura[4]: parametros[4].replace('Command: ', '').replace('com.hp.nms.incident.family.', ''),
                        estrutura[5]: hora,
                        estrutura[6]: parametros[6].replace('Command: ', '').replace('com.hp.nms.incident.family.', ''),
                        estrutura[7]: parametros[7].replace('Command: ', '').replace('com.hp.nms.incident.family.', ''),
                    })
            if(linha[:10]) == 'Started at' and captura_data:
                dic_alertas[num_alertas - 1]['hora'] = linha.split(' at ')[1]
                captura_data = False



    #Remover duplicates
    return dic_alertas

def gerar_arquivo_alertas(dic_alertas, sitescope):
    with open(sitescope + '/arquivo_alertas.txt', 'w') as saida:
        for alerta in dic_alertas:
            nome_alerta =  str(alerta).replace('\x96', '-')
            saida.write(nome_alerta + '\n')


    headers = ''
    with open(sitescope + '/arquivo_alertas_web.txt', 'w') as saida:
        for alerta in dic_alertas[:1]:
            for header in alerta.keys():
                headers += header + ','
        saida.write(headers[:-1]+'\n')

        for alerta in dic_alertas:
            valores = ''
            for valor in alerta.values():
                valores += str(valor).replace(',', ';') + ','
            #print (valores.split(','))
           # print(len(valores.split(',')))
            if len(valores.split(',')) !=10:
                pass
            else:
                saida.write(valores[:-1]+'\n')


def obter_alertas_arquivo(sitescope):
    return  [json.loads(line.rstrip('\n').replace("'", "\"")) for line in open(sitescope + '/arquivo_alertas.txt', 'r') if 'eventconsole' not in line.lower()]

def obter_monitores_arquivo(sitescope):
    return  [line.rstrip('\n') for line in open(sitescope + '/monitores.txt', 'r')]

def ordenar_monitores(lista_monitores, campo):
    if 'quantidade' in campo.lower():
        return lista_monitores
    ordenado = []
    if 'nome' in campo.lower():
        arqs = []
        for entrada in lista_monitores:
            arqs.append(entrada.split(' - ')[1] + ' - ' + entrada.split(' - ')[0])
        ordenado = []
        for o in sorted(arqs):
            ordenado.append(o.split(' - ')[1] + ' - ' + o.split(' - ')[0])

    return ordenado
def get_alertas_by(dic_alertas, campo, valor):
    filtrados = []
    for alerta in dic_alertas:
        if valor.lower() in alerta[campo].lower():
            filtrados.append(alerta)
    return filtrados

def get_quantidade_alertas(dic_alertas, name):
    quantidade = 0
    for alerta in dic_alertas:
        if alerta['alert-monitor'] == name:
            quantidade += 1

    return quantidade



if __name__ == '__main__':
    #obter_alertas_arquivo('sitescope001')

    servidores = ['nnm']

    for servidor in servidores:

        dic_alertas = popula_alertas(servidor)

        #for alerta in dic_alertas:
        #    print (len(alerta))

        gerar_arquivo_alertas(dic_alertas, servidor)




