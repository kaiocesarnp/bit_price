import requests
import pywhatkit as kit
import time

# URL da exchange para verificar o preço do Bitcoin (por exemplo, Coinbase)
url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

# Defina um limite de preço desejado
limite_preco = 30000.0  # Altere para o valor desejado

# Número de telefone para enviar a mensagem via WhatsApp
numero_whatsapp = "+5547999999999"  # Substitua pelo número desejado (inclua o código do país)

# Função para verificar o preço do Bitcoin
def verificar_preco():
    response = requests.get(url)
    data = response.json()
    preco_bitcoin = float(data["data"]["amount"])
    
    if preco_bitcoin < limite_preco:
        mensagem = f"O preço do Bitcoin está abaixo de ${limite_preco:.2f}!\nPreço atual: ${preco_bitcoin:.2f}"
        enviar_whatsapp(mensagem)

# Função para enviar mensagem via WhatsApp
def enviar_whatsapp(mensagem):
    try:
        kit.sendwhatmsg(numero_whatsapp, mensagem, time.localtime().tm_hour, time.localtime().tm_min + 2)
        print("Mensagem enviada via WhatsApp com sucesso!")
    except Exception as e:
        print("Erro ao enviar a mensagem via WhatsApp:", str(e))

#Verificação periódica do preço (por exemplo, uma vez por hora)
verificar_preco()

#Explicação do código:

#Importação de bibliotecas:
    #requests: É usado para fazer uma solicitação HTTP à API da Coinbase para obter o preço do Bitcoin.
    #pywhatkit as kit: Importa a biblioteca "pywhatkit" com um alias "kit", que é usada para enviar mensagens via WhatsApp.
    #time: É usado para trabalhar com informações de tempo, como a hora atual.

#URL da Exchange:
    #Essa linha define a URL da API da Coinbase que será usada para verificar o preço atual do Bitcoin em dólares (USD).

#Limite de preço:
    #Aqui é definido um limite de preço desejado para o Bitcoin. Se o preço cair abaixo desse limite, o código enviará uma mensagem via WhatsApp.

#Número de telefone para enviar a mensagem via WhatsApp:
    #Essa linha define o número de telefone para o qual a mensagem será enviada via WhatsApp. Substitua pelo número desejado, incluindo o código do país.

#Função para verificar o preço do Bitcoin:
    #Esta função verificar_preco() é definida para verificar o preço atual do Bitcoin na Coinbase.
    #response = requests.get(url): Nesta linha, o código faz uma solicitação HTTP GET para a URL especificada que é a URL da API da Coinbase que fornece o preço atual do Bitcoin em dólares - USD). Ele usa a biblioteca requests para realizar essa solicitação. A resposta da solicitação será armazenada na variável response.
    #data = response.json(): Após receber a resposta da solicitação, o código chama o método .json() sobre o objeto response. Isso é feito para analisar o conteúdo da resposta que é formatado em JSON. O resultado é armazenado na variável data. Agora, data conterá um dicionário Python com as informações obtidas da resposta JSON da API da Coinbase.
    #preco_bitcoin = float(data["data"]["amount"]): Esta linha extrai o preço atual do Bitcoin do dicionário data. O preço é obtido acessando a chave "data" e, em seguida, a chave "amount" dentro do dicionário. O valor desse preço é uma string, então é convertido para um número de ponto flutuante (float) usando a função float(). O resultado final é armazenado na variável preco_bitcoin.

    #Em resumo, essas três linhas de código realizam o seguinte:
    #Fazem uma solicitação GET à API da Coinbase para obter o preço atual do Bitcoin em USD.
    #Analisam a resposta JSON da API.
    #Extraem o preço do Bitcoin dessa resposta e o convertem para um número de ponto flutuante.

#Função para enviar mensagem via WhatsApp:
    #A função enviar_whatsapp() é definida para enviar mensagens via WhatsApp. Ela utiliza a biblioteca "pywhatkit" para enviar a mensagem para o número especificado (numero_whatsapp).
    #O horário de envio é definido com base na hora atual(time.localtime().tm_hour) e dois minutos a mais do minuto atual(time.localtime().tm_min + 2).
    #try:: Este é o início de um bloco try-except. O código dentro do bloco try tentará ser executado. Se ocorrer algum erro durante a execução, ele será tratado pelo bloco except
    #kit.sendwhatmsg(numero_whatsapp, mensagem, time.localtime().tm_hour, time.localtime().tm_min + 2): Esta linha chama a função sendwhatmsg da biblioteca pywhatkit (que foi importada como kit no início do código).
    #Os argumentos passados para esta função são:
    #numero_whatsapp: O número de telefone para o qual a mensagem será enviada via WhatsApp, que foi definido anteriormente no código.
    #mensagem: A mensagem que você deseja enviar.
    #time.localtime().tm_hour: A hora atual obtida através da função time.localtime().tm_hour. Isso determina a hora de envio da mensagem.
    #time.localtime().tm_min + 2: Os minutos atuais mais 2 minutos, determinando os minutos de envio da mensagem. Isso significa que a mensagem será enviada dois minutos após a hora atual.
    #print("Mensagem enviada via WhatsApp com sucesso!"): Se a mensagem for enviada com sucesso, esta linha imprime uma mensagem indicando que a mensagem foi enviada com sucesso.
    #except Exception as e: Esta parte do código é executada caso ocorra uma exceção (um erro) durante a execução do bloco try. Exception é a classe base para todas as exceções em Python, o que significa que ela capturará qualquer exceção que ocorra.
    #as e permite que você atribua a exceção capturada a uma variável chamada e, para que você possa acessar informações sobre a exceção, se necessário.
    #print("Erro ao enviar a mensagem via WhatsApp:", str(e)): Se ocorrer um erro durante o envio da mensagem, esta linha imprime uma mensagem de erro junto com uma descrição da exceção (o conteúdo da variável e), para ajudar na depuração e diagnóstico do problema

    #Em resumo, esta parte do código tenta enviar a mensagem via WhatsApp utilizando a função kit.sendwhatmsg(). Se for bem-sucedido, imprime uma mensagem de sucesso; caso contrário, imprime uma mensagem de erro com detalhes sobre a exceção que ocorreu. Isso permite lidar com possíveis erros durante o envio das mensagens.

#Verificação periódica do preço:
    #Fora das funções, o código chama a função verificar_preco() uma vez, o que verifica o preço do Bitcoin na Coinbase. Você pode ajustar a frequência dessa verificação, como mencionado no código, para executá-la periodicamente (por exemplo, uma vez por hora).
