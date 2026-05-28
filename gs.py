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

listanalisedesastre = []

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
    texto = ("O projeto Orbitguard analisa dados climáticos para apoiar a produção agrícola.\n"
        "O sistema cadastra plantações e avalia riscos de temperatura, umidade e chuva.\n"
        "Com base nas análises, gera recomendações agrícolas para reduzir perdas.\n"
        "A solução usa listas e funções em Python para organizar informações.\n"
        "Assim, contribui para prevenir desastres naturais e proteger a produção agrícola."
    )
    return texto

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

        listanalisedesastre.append('')

        titulo('PLANTAÇÃO CADASTRADA')

        return (f'Plantil: {listplantil[-1]}\n'
                f'Temperatura: {listtemperatura[-1]}°C\n'
                f'Umidade do solo: {listumidade[-1]}%\n'
                f'Chuva prevista: {listquantidadechuva[-1]}%\n'
                f'Região: {listregiao[-1]}')

def analiseclimatica():

    titulo('CADASTROS DISPONÍVEIS PARA ANÁLISE')

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

        elif listtemperatura[indice] >= 28 and listtemperatura[indice] <= 35:
            analisetemperatura = 'Moderado'

        else:
            analisetemperatura = 'Baixo'

        if listumidade[indice] < 30:
            analiseumidade = 'Baixo'

        elif listumidade[indice] >= 30 and listumidade[indice] <= 50:
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

def desastresnaturais():

    titulo('CADASTROS DISPONÍVEIS PARA ANÁLISE')

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

        if listinterpretacao[indice] == 'Forte risco de seca agrícola e estresse hídrico':
            desastrenatural = 'Seca agrícola severa'

        elif listinterpretacao[indice] == 'Calor elevado e solo seco, com necessidade de irrigação':
            desastrenatural = 'Onda de calor agrícola'

        elif listinterpretacao[indice] == 'Calor elevado com solo seco, mas há risco de chuva intensa':
            desastrenatural = 'Erosão após solo ressecado'

        elif listinterpretacao[indice] == 'Temperatura elevada e pouca chuva podem iniciar seca agrícola':
            desastrenatural = 'Estiagem inicial'

        elif listinterpretacao[indice] == 'Possível estresse térmico, mas com condições parcialmente controladas':
            desastrenatural = 'Estresse térmico agrícola'

        elif listinterpretacao[indice] == 'Temperatura elevada associada a chuva intensa pode afetar o solo':
            desastrenatural = 'Tempestade agrícola'

        elif listinterpretacao[indice] == 'Calor elevado, mas a umidade ainda reduz o risco imediato de seca':
            desastrenatural = 'Calor úmido'

        elif listinterpretacao[indice] == 'Temperatura elevada com boa disponibilidade de umidade no solo':
            desastrenatural = 'Ambiente propício a pragas'

        elif listinterpretacao[indice] == 'Calor e excesso de água podem favorecer doenças e encharcamento':
            desastrenatural = 'Fungos e encharcamento'

        elif listinterpretacao[indice] == 'Solo seco e baixa chuva indicam risco de seca agrícola':
            desastrenatural = 'Estiagem agrícola'

        elif listinterpretacao[indice] == 'Solo seco, mas com alguma previsão de chuva':
            desastrenatural = 'Déficit hídrico moderado'

        elif listinterpretacao[indice] == 'Solo seco com chuva intensa pode gerar erosão e perda de nutrientes':
            desastrenatural = 'Erosão do solo'

        elif listinterpretacao[indice] == 'Baixa chuva exige acompanhamento da umidade do solo':
            desastrenatural = 'Estiagem leve'

        elif listinterpretacao[indice] == 'Condições agrícolas estáveis e aceitáveis':
            desastrenatural = 'Sem desastre identificado'

        elif listinterpretacao[indice] == 'Chuva elevada exige atenção à drenagem do solo':
            desastrenatural = 'Alagamento leve'

        elif listinterpretacao[indice] == 'Boa umidade do solo mesmo com baixa chuva prevista':
            desastrenatural = 'Sem desastre imediato'

        elif listinterpretacao[indice] == 'Condição favorável ao desenvolvimento da plantação':
            desastrenatural = 'Sem desastre identificado'

        elif listinterpretacao[indice] == 'Excesso de umidade e chuva pode favorecer doenças e encharcamento':
            desastrenatural = 'Encharcamento agrícola'

        elif listinterpretacao[indice] == 'Frio associado a solo seco e pouca chuva pode prejudicar a cultura':
            desastrenatural = 'Frio seco agrícola'

        elif listinterpretacao[indice] == 'Temperatura baixa e solo seco exigem acompanhamento':
            desastrenatural = 'Estresse por frio'

        elif listinterpretacao[indice] == 'Frio com chuva intensa pode prejudicar o solo e a cultura':
            desastrenatural = 'Tempestade fria'

        elif listinterpretacao[indice] == 'Temperatura baixa pode afetar culturas sensíveis':
            desastrenatural = 'Geada leve / frio intenso'

        elif listinterpretacao[indice] == 'Frio moderado exige atenção conforme a cultura plantada':
            desastrenatural = 'Frio agrícola moderado'

        elif listinterpretacao[indice] == 'Frio e chuva intensa podem causar encharcamento e prejudicar a cultura':
            desastrenatural = 'Encharcamento com frio'

        elif listinterpretacao[indice] == 'Temperatura baixa com umidade elevada pode favorecer doenças':
            desastrenatural = 'Doenças fúngicas'

        elif listinterpretacao[indice] == 'Frio e umidade elevada exigem acompanhamento da cultura':
            desastrenatural = 'Frio úmido'

        elif listinterpretacao[indice] == 'Frio, alta umidade e chuva intensa aumentam risco de doenças e encharcamento':
            desastrenatural = 'Encharcamento severo / fungos'

        else:
            desastrenatural = 'Nenhum desastre natural específico encontrado. Verifique se a análise climática foi realizada corretamente.'

        listanalisedesastre[indice] = desastrenatural

        return (f'\n{"=" * 50}\n'
                f'{"RESULTADO DA ANÁLISE DE DESASTRE NATURAL".center(50)}\n'
                f'{"=" * 50}\n'
                f'Plantil: {listplantil[indice]}\n'
                f'Temperatura: {listtemperatura[indice]}\n'
                f'Umidade: {listumidade[indice]}\n'
                f'Chuva: {listquantidadechuva[indice]}\n'
                f'\nRisco geral: {listrisco[indice]}\n'
                f'Interpretação: {listinterpretacao[indice]}\n'
                f'\nDesastre natural indentificado: {desastrenatural}\n'
                f'{"=" * 50}')



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

        if listrisco[indice] == 'Crítico' and listanalisedesastre[indice] == 'Seca agrícola severa':
            recomendacaoagr = 'Emitir alerta de seca severa, priorizar irrigação emergencial e monitorar diariamente a umidade do solo'

        elif listrisco[indice] == 'Alto' and listanalisedesastre[indice] == 'Onda de calor agrícola':
            recomendacaoagr = 'Reforçar irrigação preventiva e intensificar o monitoramento contra onda de calor agrícola'

        elif listrisco[indice] == 'Alto' and listanalisedesastre[indice] == 'Erosão após solo ressecado':
            recomendacaoagr = 'Preparar drenagem do solo e evitar manejo pesado, pois há risco de erosão após período seco'

        elif listrisco[indice] == 'Alto' and listanalisedesastre[indice] == 'Estiagem inicial':
            recomendacaoagr = 'Planejar uso racional da água e acompanhar possível evolução para estiagem agrícola'

        elif listrisco[indice] == 'Moderado' and listanalisedesastre[indice] == 'Estresse térmico agrícola':
            recomendacaoagr = 'Manter irrigação controlada e acompanhar sinais de estresse térmico na plantação'

        elif listrisco[indice] == 'Alto' and listanalisedesastre[indice] == 'Tempestade agrícola':
            recomendacaoagr = 'Evitar irrigação adicional e verificar áreas com risco de tempestade agrícola e erosão'

        elif listrisco[indice] == 'Moderado' and listanalisedesastre[indice] == 'Calor úmido':
            recomendacaoagr = 'Monitorar o calor úmido e acompanhar a umidade do solo para evitar estresse futuro'

        elif listrisco[indice] == 'Moderado' and listanalisedesastre[indice] == 'Ambiente propício a pragas':
            recomendacaoagr = 'Manter monitoramento climático e observar possível aumento de pragas em ambiente quente e úmido'

        elif listrisco[indice] == 'Alto' and listanalisedesastre[indice] == 'Fungos e encharcamento':
            recomendacaoagr = 'Acionar manejo preventivo contra fungos, verificar drenagem e evitar excesso de água no solo'

        elif listrisco[indice] == 'Alto' and listanalisedesastre[indice] == 'Estiagem agrícola':
            recomendacaoagr = 'Acionar plano de irrigação e acompanhar a evolução da estiagem agrícola'

        elif listrisco[indice] == 'Moderado' and listanalisedesastre[indice] == 'Déficit hídrico moderado':
            recomendacaoagr = 'Monitorar o solo e aguardar confirmação da chuva antes de alterar o manejo da irrigação'

        elif listrisco[indice] == 'Alto' and listanalisedesastre[indice] == 'Erosão do solo':
            recomendacaoagr = 'Proteger o solo, preparar drenagem e evitar uso de máquinas para reduzir risco de erosão'

        elif listrisco[indice] == 'Moderado' and listanalisedesastre[indice] == 'Estiagem leve':
            recomendacaoagr = 'Acompanhar umidade do solo e planejar irrigação preventiva contra estiagem leve'

        elif listrisco[indice] == 'Baixo' and listanalisedesastre[indice] == 'Sem desastre identificado':
            recomendacaoagr = 'Manter monitoramento periódico, sem necessidade de ação emergencial'

        elif listrisco[indice] == 'Moderado' and listanalisedesastre[indice] == 'Alagamento leve':
            recomendacaoagr = 'Verificar drenagem e acompanhar pontos de acúmulo de água para evitar alagamento leve'

        elif listrisco[indice] == 'Baixo' and listanalisedesastre[indice] == 'Sem desastre imediato':
            recomendacaoagr = 'Manter acompanhamento da umidade do solo, sem alerta de desastre imediato'

        elif listrisco[indice] == 'Alto' and listanalisedesastre[indice] == 'Encharcamento agrícola':
            recomendacaoagr = 'Melhorar drenagem e monitorar doenças fúngicas associadas ao encharcamento agrícola'

        elif listrisco[indice] == 'Alto' and listanalisedesastre[indice] == 'Frio seco agrícola':
            recomendacaoagr = 'Verificar sensibilidade da cultura ao frio seco e manter irrigação controlada'

        elif listrisco[indice] == 'Moderado' and listanalisedesastre[indice] == 'Estresse por frio':
            recomendacaoagr = 'Monitorar o solo e proteger culturas sensíveis contra estresse por frio'

        elif listrisco[indice] == 'Alto' and listanalisedesastre[indice] == 'Tempestade fria':
            recomendacaoagr = 'Evitar manejo no solo molhado e acompanhar risco de tempestade fria agrícola'

        elif listrisco[indice] == 'Moderado' and listanalisedesastre[indice] == 'Geada leve / frio intenso':
            recomendacaoagr = 'Verificar sensibilidade da cultura e acompanhar risco de geada leve ou frio intenso'

        elif listrisco[indice] == 'Moderado' and listanalisedesastre[indice] == 'Frio agrícola moderado':
            recomendacaoagr = 'Acompanhar temperatura e avaliar necessidade de proteção para culturas sensíveis'

        elif listrisco[indice] == 'Alto' and listanalisedesastre[indice] == 'Encharcamento com frio':
            recomendacaoagr = 'Verificar drenagem, evitar operações no solo e monitorar encharcamento com frio'

        elif listrisco[indice] == 'Moderado' and listanalisedesastre[indice] == 'Doenças fúngicas':
            recomendacaoagr = 'Monitorar doenças fúngicas e evitar excesso de água em condição de frio úmido'

        elif listrisco[indice] == 'Moderado' and listanalisedesastre[indice] == 'Frio úmido':
            recomendacaoagr = 'Acompanhar desenvolvimento da cultura e monitorar sinais de frio úmido'

        elif listrisco[indice] == 'Alto' and listanalisedesastre[indice] == 'Encharcamento severo / fungos':
            recomendacaoagr = 'Melhorar drenagem, evitar manejo no solo e monitorar doenças associadas ao encharcamento severo'

        else:
            recomendacaoagr = 'Nenhuma recomendação específica encontrada. Faça primeiro a análise climática e a análise de desastres naturais.'

        listrecomendacao[indice] = recomendacaoagr

        return (f'\n{"=" * 50}\n'
                f'{"RECOMENDAÇÃO AGRÍCOLA".center(50)}\n'
                f'{"=" * 50}\n'
                f'Plantil: {listplantil[indice]}\n'
                f'Risco geral: {listrisco[indice]}\n'
                f'Desastre natural: {listanalisedesastre[indice]}\n'
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
        print(f'Desastre natural: {listanalisedesastre[i]}')

        subtitulo('Recomendação')
        print(f'{listrecomendacao[i]}')

        linha()

    return ''


def main():
    while True:
        titulo('ORBITGUARD')

        print('1 - Descrição da solução')
        print('2 - Cadastrar dados da plantação')
        print('3 - Analisar risco climático')
        print('4 - Analisar risco de desastre natural')
        print('5 - Gerar recomendação agrícola')
        print('6 - Exibir relatório geral')
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
                print(desastresnaturais())

            case 5:
                print(recomendacoa())

            case 6:
                print(relatorio())

            case 0:
                print('\nSistema encerrado. Obrigado por usar o AgroSat Monitor!')
                break

            case _:
                print('\nOpção inválida. Tente novamente.')

main()