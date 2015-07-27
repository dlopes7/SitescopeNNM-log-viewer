import re
import json
import time


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

    novo = False

    pattern = re.compile(' alert-(.*?): ')

    try:
        alertas = open(sitescope + '/alert.log.old', 'r', encoding="utf-8")
        linhas = alertas.readlines()
    except UnicodeDecodeError:
        alertas = open(sitescope + '/alert.log.old', 'r', encoding="latin-1")
        linhas = alertas.readlines()


    for linha in linhas:
        linha = linha.replace('\x96', '-')
        if not pattern.match(linha):
            novo = False

        if '\talert\n' in linha:
            hora = linha.rstrip('\talert\n')
            dic_alertas.append({'hora':hora})
            novo = True
            num_alertas += 1

        if novo and pattern.match(linha):
            atributo, valor  = linha.rstrip('\n').split(': ')[:2]
            dic_alertas[num_alertas - 1][atributo.lstrip(' ')] = valor.rstrip('\n')

    try:
        alertas = open(sitescope + '/alert.log', 'r', encoding="utf-8")
        linhas = alertas.readlines()
    except UnicodeDecodeError:
        alertas = open(sitescope + '/alert.log', 'r', encoding="latin-1")
        linhas = alertas.readlines()


    for linha in linhas:
        linha = linha.replace('\x96', '-')
        if not pattern.match(linha):
            novo = False

        if '\talert\n' in linha:
            hora = linha.rstrip('\talert\n')
            dic_alertas.append({'hora':hora})
            novo = True
            num_alertas += 1

        if novo and pattern.match(linha):
            atributo, valor  = linha.rstrip('\n').split(': ')[:2]
            dic_alertas[num_alertas - 1][atributo.lstrip(' ')] = valor.rstrip('\n')

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
                valores += valor.replace(',', ';').replace('\x96', '-') + ','
            if len(valores.split(',')) != 9:
                print (valores)
            else:
                saida.write(valores[:-1]+'\n')


def gerar_arquivo_unicos(dic_alertas, sitescope):
    print(sitescope + '\t\tLendo o arquivo (' + str(len(dic_alertas)) + ') entradas...' )
    monitores = []
    for alerta in dic_alertas:
        monitores.append(alerta['alert-monitor'])


    print(sitescope + '\t\tCalculando a quantidade de alertas por monitor (' + str(len(monitores)) + ') alertas...' )
    monitores_quantidade = []
    for nome_alerta in del_dups(monitores):
        monitores_quantidade.append([(get_quantidade_alertas(dic_alertas, nome_alerta)), nome_alerta])

    ordenados = sorted(monitores_quantidade, reverse=True)

    print (sitescope + '\t\tEscrevendo saida (' + str(len(ordenados)) + ') monitores...')
    with open(sitescope + '/monitores.txt', 'w') as arq_monitores:
        for alerta in ordenados:
           nome_alerta = alerta[1].replace('\x96', '-')
           arq_monitores.write('(' + str(alerta[0])  + ') - ' + nome_alerta + '\n')

def obter_alertas_arquivo(sitescope):
    return  [json.loads(line.rstrip('\n').replace("'", "\"")) for line in open(sitescope + '/arquivo_alertas.txt', 'r')  if 'eventconsole' not in line.lower()]

def obter_monitores_arquivo(sitescope):
    return  [line.rstrip('\n') for line in open(sitescope + '/monitores.txt', 'r')]

def ordenar_monitores(lista_monitores, campo):
    if 'quantidade' in campo.lower():
        return lista_monitores

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

def get_unique_alerts(dic_alertas):

    monitores = []
    for alerta in dic_alertas:
        monitores.append(alerta['alert-monitor'])

    monitores_quantidade = []
    for nome_alerta in set(monitores):
        monitores_quantidade.append([(get_quantidade_alertas(dic_alertas, nome_alerta)), nome_alerta])

    lista_formatada = []
    for alerta in sorted(monitores_quantidade, reverse=True):
        lista_formatada.append('(' + str(alerta[0]) + ') - ' + alerta[1])

    return lista_formatada


if __name__ == '__main__':
    #obter_alertas_arquivo('sitescope001')

    sitescopes = ['sitescope001',
                  'sitescope002',
                  'sitescope003',
                  'sitescope004',
                  ]

    for sitescope in sitescopes:
        print('')
        print ('INICIO')
        print (sitescope + '\tProcessando arquivos de log...')
        dic_alertas = popula_alertas(sitescope)

        print (sitescope + '\tFormatando saida...')
        gerar_arquivo_alertas(dic_alertas, sitescope)

        print (sitescope + '\tGerando monitores...')
        gerar_arquivo_unicos(dic_alertas, sitescope)

        print ('TERMINADO')




