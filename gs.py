listnumeracao = []
listplantil = []
listtemperatura = []
listumidade = []
listquantidadechuva = []
listregiao = []

listanalisetemperatura = []
listanaliseumidade = []
listanalisequantidadechuva = []
listrisco = []
listinterpretacao  = []

listrecomendacao = []

def linha():
    print('-' * 50)

def titulo(texto):
    print('\n' + '=' * 50)
    print(texto.center(50))
    print('=' * 50)

def subtitulo(texto):
    print('\n' + texto.upper())
    print('-' * 50)

def descricaosolucao():
    return 'teste'

def cadastro():

    numeracao = int(input('Informe uma numeração para este cadastro:'))

    if numeracao in listnumeracao:
        return 'Essa numeração já existe!'

    else:
        plantil = input('Nome do plantil: ')
        temperatura = float(input('Temperatura: '))
        umidade = float(input('Umidade do solo: '))
        quantidadechuva = float(input('Chuva prevista(porcentagem): '))
        regiao = input('Região: ')

        listnumeracao.append(numeracao)
        listplantil.append(plantil)
        listtemperatura.append(temperatura)
        listumidade.append(umidade)
        listquantidadechuva.append(quantidadechuva)
        listregiao.append(regiao)

        listrisco.append('')
        listinterpretacao.append('')
        listanalisetemperatura.append('')
        listanaliseumidade.append('')
        listanalisequantidadechuva.append('')
        listrecomendacao.append('')

        titulo('PLANTAÇÃO CADASTRADA')

        return (f'Plantil: {listplantil[-1]}\n'
                f'Temperatura: {listtemperatura[-1]}°C\n'
                f'Umidade do solo: {listumidade[-1]}%\n'
                f'Chuva prevista: {listquantidadechuva[-1]}%\n'
                f'Região: {listregiao[-1]}')

def analiseclimatica():

    titulo('CADASTROS DISPONÍVEIS')

    for i in range(len(listnumeracao)):
        print(f'Cadastro #{listnumeracao[i]}')
        print(f'Plantil: {listplantil[i]}')
        linha()

    opcao = int(input('\nDigite a numeração do cadastro que deseja analisar: '))

    if opcao in listnumeracao:
        indice = listnumeracao.index(opcao)
        print(f'\nPlantil: {listplantil[indice]}')
        print(f'Temperatura: {listtemperatura[indice]}°C')
        print(f'Umidade: {listumidade[indice]}%')
        print(f'Quantidade: {listquantidadechuva[indice]}%')

        if listtemperatura[indice] > 35:
            analisetemperatura = 'Alta'

        elif listtemperatura[indice] > 28 and listtemperatura[indice] < 35:
            analisetemperatura = 'Moderado'

        else:
            analisetemperatura = 'Baixo'

        if listumidade[indice] < 30:
            analiseumidade = 'Baixo'

        elif listumidade[indice] > 30 and listumidade[indice] < 50:
            analiseumidade = 'Moderado'

        else:
            analiseumidade = 'Alta'

        if listquantidadechuva[indice] > 80:
            analisequantidadechuva = 'Alta'

        elif listquantidadechuva[indice] > 40 and listquantidadechuva[indice] < 80:
            analisequantidadechuva = 'Moderado'

        else:
            analisequantidadechuva = 'Baixo'

        listanalisetemperatura[indice] = analisetemperatura
        listanaliseumidade[indice] = analiseumidade
        listanalisequantidadechuva[indice] = analisequantidadechuva

        if analisetemperatura == 'Alta' and analiseumidade == 'Baixo' and analisequantidadechuva == 'Baixo':
            risco = 'Crítico'
            interpretacao = 'Forte risco de seca agrícola e estresse hídrico'

        elif analisetemperatura == 'Alta' and analiseumidade == 'Baixo' and analisequantidadechuva == 'Moderado':
            risco = 'Alto'
            interpretacao = 'Calor elevado e solo seco, com necessidade de irrigação'

        elif analisetemperatura == 'Alta' and analiseumidade == 'Baixo' and analisequantidadechuva == 'Alta':
            risco = 'Alto'
            interpretacao = 'Calor elevado com solo seco, mas há risco de chuva intensa'

        elif analisetemperatura == 'Alta' and analiseumidade == 'Moderado' and analisequantidadechuva == 'Baixo':
            risco = 'Alto'
            interpretacao = 'Temperatura elevada e pouca chuva podem iniciar seca agrícola'

        elif analisetemperatura == 'Alta' and analiseumidade == 'Moderado' and analisequantidadechuva == 'Moderado':
            risco = 'Moderado'
            interpretacao = 'Possível estresse térmico, mas com condições parcialmente controladas'

        elif analisetemperatura == 'Alta' and analiseumidade == 'Moderado' and analisequantidadechuva == 'Alta':
            risco = 'Alto'
            interpretacao = 'Temperatura elevada associada a chuva intensa pode afetar o solo'

        elif analisetemperatura == 'Alta' and analiseumidade == 'Alta' and analisequantidadechuva == 'Baixo':
            risco = 'Moderado'
            interpretacao = 'Calor elevado, mas a umidade ainda reduz o risco imediato de seca'

        elif analisetemperatura == 'Alta' and analiseumidade == 'Alta' and analisequantidadechuva == 'Moderado':
            risco = 'Moderado'
            interpretacao = 'Temperatura elevada com boa disponibilidade de umidade no solo'

        elif analisetemperatura == 'Alta' and analiseumidade == 'Alta' and analisequantidadechuva == 'Alta':
            risco = 'Alto'
            interpretacao = 'Calor e excesso de água podem favorecer doenças e encharcamento'

        elif analisetemperatura == 'Moderado' and analiseumidade == 'Baixo' and analisequantidadechuva == 'Baixo':
            risco = 'Alto'
            interpretacao = 'Solo seco e baixa chuva indicam risco de seca agrícola'

        elif analisetemperatura == 'Moderado' and analiseumidade == 'Baixo' and analisequantidadechuva == 'Moderado':
            risco = 'Moderado'
            interpretacao = 'Solo seco, mas com alguma previsão de chuva'

        elif analisetemperatura == 'Moderado' and analiseumidade == 'Baixo' and analisequantidadechuva == 'Alta':
            risco = 'Alto'
            interpretacao = 'Solo seco com chuva intensa pode gerar erosão e perda de nutrientes'

        elif analisetemperatura == 'Moderado' and analiseumidade == 'Moderado' and analisequantidadechuva == 'Baixo':
            risco = 'Moderado'
            interpretacao = 'Baixa chuva exige acompanhamento da umidade do solo'

        elif analisetemperatura == 'Moderado' and analiseumidade == 'Moderado' and analisequantidadechuva == 'Moderado':
            risco = 'Baixo'
            interpretacao = 'Condições agrícolas estáveis e aceitáveis'

        elif analisetemperatura == 'Moderado' and analiseumidade == 'Moderado' and analisequantidadechuva == 'Alta':
            risco = 'Moderado'
            interpretacao = 'Chuva elevada exige atenção à drenagem do solo'

        elif analisetemperatura == 'Moderado' and analiseumidade == 'Alta' and analisequantidadechuva == 'Baixo':
            risco = 'Baixo'
            interpretacao = 'Boa umidade do solo mesmo com baixa chuva prevista'

        elif analisetemperatura == 'Moderado' and analiseumidade == 'Alta' and analisequantidadechuva == 'Moderado':
            risco = 'Baixo'
            interpretacao = 'Condição favorável ao desenvolvimento da plantação'

        elif analisetemperatura == 'Moderado' and analiseumidade == 'Alta' and analisequantidadechuva == 'Alta':
            risco = 'Alto'
            interpretacao = 'Excesso de umidade e chuva pode favorecer doenças e encharcamento'

        elif analisetemperatura == 'Baixo' and analiseumidade == 'Baixo' and analisequantidadechuva == 'Baixo':
            risco = 'Alto'
            interpretacao = 'Frio associado a solo seco e pouca chuva pode prejudicar a cultura'

        elif analisetemperatura == 'Baixo' and analiseumidade == 'Baixo' and analisequantidadechuva == 'Moderado':
            risco = 'Moderado'
            interpretacao = 'Temperatura baixa e solo seco exigem acompanhamento'

        elif analisetemperatura == 'Baixo' and analiseumidade == 'Baixo' and analisequantidadechuva == 'Alta':
            risco = 'Alto'
            interpretacao = 'Frio com chuva intensa pode prejudicar o solo e a cultura'

        elif analisetemperatura == 'Baixo' and analiseumidade == 'Moderado' and analisequantidadechuva == 'Baixo':
            risco = 'Moderado'
            interpretacao = 'Temperatura baixa pode afetar culturas sensíveis'

        elif analisetemperatura == 'Baixo' and analiseumidade == 'Moderado' and analisequantidadechuva == 'Moderado':
            risco = 'Moderado'
            interpretacao = 'Frio moderado exige atenção conforme a cultura plantada'

        elif analisetemperatura == 'Baixo' and analiseumidade == 'Moderado' and analisequantidadechuva == 'Alta':
            risco = 'Alto'
            interpretacao = 'Frio e chuva intensa podem causar encharcamento e prejudicar a cultura'

        elif analisetemperatura == 'Baixo' and analiseumidade == 'Alta' and analisequantidadechuva == 'Baixo':
            risco = 'Moderado'
            interpretacao = 'Temperatura baixa com umidade elevada pode favorecer doenças'

        elif analisetemperatura == 'Baixo' and analiseumidade == 'Alta' and analisequantidadechuva == 'Moderado':
            risco = 'Moderado'
            interpretacao = 'Frio e umidade elevada exigem acompanhamento da cultura'

        elif analisetemperatura == 'Baixo' and analiseumidade == 'Alta' and analisequantidadechuva == 'Alta':
            risco = 'Alto'
            interpretacao = 'Frio, alta umidade e chuva intensa aumentam risco de doenças e encharcamento'

        else:
            risco = 'Baixo'
            interpretacao = 'Condições climáticas estáveis'

        listrisco[indice] = risco
        listinterpretacao[indice] = interpretacao

        return (f'\n{"=" * 50}\n'
                f'{"RESULTADO DA ANÁLISE CLIMÁTICA".center(50)}\n'
                f'{"=" * 50}\n'
                f'Plantil: {listplantil[indice]}\n'
                f'Temperatura: {analisetemperatura}\n'
                f'Umidade: {analiseumidade}\n'
                f'Chuva: {analisequantidadechuva}\n'
                f'\nRisco geral: {risco}\n'
                f'Interpretação: {interpretacao}\n'
                f'{"=" * 50}')


    else:
        return '\nNenhum cadastro encontrado para fazer a análise.'

def recomendacoa():

    titulo('RECOMENDAÇÕES DISPONÍVEIS')

    for i in range(len(listnumeracao)):
        print(f'Cadastro #{listnumeracao[i]}')
        print(f'Plantil: {listplantil[i]}')
        linha()

    opcao = int(input('\nDigite a numeração do cadastro para gerar recomendação: '))

    if opcao in listnumeracao:
        indice = listnumeracao.index(opcao)
        print(f'\nPlantil: {listplantil[indice]}')
        print(f'Temperatura: {listtemperatura[indice]}°C')
        print(f'Umidade: {listumidade[indice]}%')
        print(f'Quantidade: {listquantidadechuva[indice]}%')
        print()
        print('SITUAÇÃO CLIMÁTICA:')
        print(f'A temperatura está: {listanalisetemperatura[indice]}')
        print(f'A umidade está: {listanaliseumidade[indice]}%')
        print(f'A chuva está: {listanalisequantidadechuva[indice]}')
        print()
        print(f'Risco geral da plantação: {listrisco[indice]} ')
        print(f'Interpretação da plantação: {listinterpretacao[indice]}')

        if listrisco[indice] == 'Crítico' and listinterpretacao[indice] == 'Forte risco de seca agrícola e estresse hídrico':
            recomendacaoagr = 'Emitir alerta crítico, priorizar irrigação e monitorar diariamente a plantação'

        elif listrisco[indice] == 'Alto' and listinterpretacao[indice] == 'Calor elevado e solo seco, com necessidade de irrigação':
            recomendacaoagr = 'Reforçar irrigação e acompanhar a previsão climática'

        elif listrisco[indice] == 'Alto' and listinterpretacao[indice] == 'Calor elevado com solo seco, mas há risco de chuva intensa':
            recomendacaoagr = 'Monitorar irrigação e preparar drenagem para possível chuva forte'

        elif listrisco[indice] == 'Alto' and listinterpretacao[indice] == 'Temperatura elevada e pouca chuva podem iniciar seca agrícola':
            recomendacaoagr = 'Planejar uso de água e evitar plantio em curto prazo'

        elif listrisco[indice] == 'Moderado' and listinterpretacao[indice] == 'Possível estresse térmico, mas com condições parcialmente controladas':
            recomendacaoagr = 'Acompanhar temperatura e manter irrigação controlada'

        elif listrisco[indice] == 'Alto' and listinterpretacao[indice] == 'Temperatura elevada associada a chuva intensa pode afetar o solo':
            recomendacaoagr = 'Evitar irrigação extra e verificar drenagem do solo'

        elif listrisco[indice] == 'Moderado' and listinterpretacao[indice] == 'Calor elevado, mas a umidade ainda reduz o risco imediato de seca':
            recomendacaoagr = 'Monitorar temperatura e manter acompanhamento da umidade'

        elif listrisco[indice] == 'Moderado' and listinterpretacao[indice] == 'Temperatura elevada com boa disponibilidade de umidade no solo':
            recomendacaoagr = 'Manter monitoramento climático e evitar irrigação excessiva'

        elif listrisco[indice] == 'Alto' and listinterpretacao[indice] == 'Calor e excesso de água podem favorecer doenças e encharcamento':
            recomendacaoagr = 'Verificar drenagem e acompanhar sinais de doenças na cultura'

        elif listrisco[indice] == 'Alto' and listinterpretacao[indice] == 'Solo seco e baixa chuva indicam risco de seca agrícola':
            recomendacaoagr = 'Acionar plano de irrigação e acompanhar previsão de chuva'

        elif listrisco[indice] == 'Moderado' and listinterpretacao[indice] == 'Solo seco, mas com alguma previsão de chuva':
            recomendacaoagr = 'Monitorar o solo e aguardar confirmação da chuva prevista'

        elif listrisco[indice] == 'Alto' and listinterpretacao[indice] == 'Solo seco com chuva intensa pode gerar erosão e perda de nutrientes':
            recomendacaoagr = 'Preparar drenagem e evitar manejo pesado no solo'

        elif listrisco[indice] == 'Moderado' and listinterpretacao[indice] == 'Baixa chuva exige acompanhamento da umidade do solo':
            recomendacaoagr = 'Acompanhar umidade e planejar irrigação preventiva'

        elif listrisco[indice] == 'Baixo' and listinterpretacao[indice] == 'Condições agrícolas estáveis e aceitáveis':
            recomendacaoagr = 'Manter monitoramento periódico'

        elif listrisco[indice] == 'Moderado' and listinterpretacao[indice] == 'Chuva elevada exige atenção à drenagem do solo':
            recomendacaoagr = 'Verificar drenagem e evitar excesso de irrigação'

        elif listrisco[indice] == 'Baixo' and listinterpretacao[indice] == 'Boa umidade do solo mesmo com baixa chuva prevista':
            recomendacaoagr = 'Manter acompanhamento da umidade do solo'

        elif listrisco[indice] == 'Baixo' and listinterpretacao[indice] == 'Condição favorável ao desenvolvimento da plantação':
            recomendacaoagr = 'Manter manejo atual e monitoramento climático'

        elif listrisco[indice] == 'Alto' and listinterpretacao[indice] == 'Excesso de umidade e chuva pode favorecer doenças e encharcamento':
            recomendacaoagr = 'Melhorar drenagem e monitorar doenças fúngicas'

        elif listrisco[indice] == 'Alto' and listinterpretacao[indice] == 'Frio associado a solo seco e pouca chuva pode prejudicar a cultura':
            recomendacaoagr = 'Verificar sensibilidade da cultura e planejar irrigação controlada'

        elif listrisco[indice] == 'Moderado' and listinterpretacao[indice] == 'Temperatura baixa e solo seco exigem acompanhamento':
            recomendacaoagr = 'Monitorar solo e proteger culturas sensíveis ao frio'

        elif listrisco[indice] == 'Alto' and listinterpretacao[indice] == 'Frio com chuva intensa pode prejudicar o solo e a cultura':
            recomendacaoagr = 'Evitar manejo no solo molhado e proteger culturas sensíveis'

        elif listrisco[indice] == 'Moderado' and listinterpretacao[indice] == 'Temperatura baixa pode afetar culturas sensíveis':
            recomendacaoagr = 'Verificar sensibilidade da cultura plantada'

        elif listrisco[indice] == 'Moderado' and listinterpretacao[indice] == 'Frio moderado exige atenção conforme a cultura plantada':
            recomendacaoagr = 'Acompanhar temperatura e avaliar proteção da cultura'

        elif listrisco[indice] == 'Alto' and listinterpretacao[indice] == 'Frio e chuva intensa podem causar encharcamento e prejudicar a cultura':
            recomendacaoagr = 'Verificar drenagem e evitar operações no solo'

        elif listrisco[indice] == 'Moderado' and listinterpretacao[indice] == 'Temperatura baixa com umidade elevada pode favorecer doenças':
            recomendacaoagr = 'Monitorar doenças e evitar excesso de água'

        elif listrisco[indice] == 'Moderado' and listinterpretacao[indice] == 'Frio e umidade elevada exigem acompanhamento da cultura':
            recomendacaoagr = 'Acompanhar desenvolvimento da cultura e monitorar umidade'

        elif listrisco[indice] == 'Alto' and listinterpretacao[indice] == 'Frio, alta umidade e chuva intensa aumentam risco de doenças e encharcamento':
            recomendacaoagr = 'Melhorar drenagem, evitar manejo no solo e monitorar doenças'

        else:
            recomendacaoagr = 'Nenhuma recomendação específica encontrada. Verifique se a análise climática foi realizada corretamente.'

        listrecomendacao[indice] = recomendacaoagr

    return (f'\n{"=" * 50}\n'
            f'{"RECOMENDAÇÃO AGRÍCOLA".center(50)}\n'
            f'{"=" * 50}\n'
            f'Plantil: {listplantil[indice]}\n'
            f'Risco geral: {listrisco[indice]}\n'
            f'\nRecomendação:\n{recomendacaoagr}\n'
            f'{"=" * 50}')

def relatorio():

    if len(listnumeracao) == 0:
        return '\nNenhum cadastro encontrado.'

    titulo('RELATÓRIO GERAL')

    for i in range(len(listnumeracao)):
        print(f'Cadastro #{listnumeracao[i]}')
        print(f'Plantil: {listplantil[i]}')
        print(f'Região: {listregiao[i]}')
        print(f'Temperatura: {listtemperatura[i]}°C')
        print(f'Umidade do solo: {listumidade[i]}%')
        print(f'Chuva prevista: {listquantidadechuva[i]}%')

        subtitulo('Situação Climática')
        print(f'Temperatura: {listanalisetemperatura[i]}')
        print(f'Umidade: {listanaliseumidade[i]}')
        print(f'Chuva: {listanalisequantidadechuva[i]}')

        subtitulo('Resultado')
        print(f'Risco geral: {listrisco[i]}')
        print(f'Interpretação: {listinterpretacao[i]}')

        subtitulo('Recomendação')
        print(f'{listrecomendacao[i]}')

        linha()

    return ''


def main():
    while True:
        titulo('AGROSAT MONITOR')

        print('1 - Descrição da solução')
        print('2 - Cadastrar dados da plantação')
        print('3 - Analisar risco climático')
        print('4 - Gerar recomendação agrícola')
        print('5 - Exibir relatório geral')
        print('0 - Sair')

        opcao = int(input('\nDigite o código da opção desejada: '))

        match opcao:
            case 1:
                titulo('DESCRIÇÃO DA SOLUÇÃO')
                print(descricaosolucao())

            case 2:
                titulo('CADASTRO DE DADOS DA PLANTAÇÃO')
                print(cadastro())

            case 3:
                print(analiseclimatica())

            case 4:
                print(recomendacoa())

            case 5:
                print(relatorio())

            case 0:
                print('\nSistema encerrado. Obrigado por usar o AgroSat Monitor!')
                break

            case _:
                print('\nOpção inválida. Tente novamente.')

main()