import random, string

tamanho = int(input("Digite o tamanho de senha que você deseja: "))
chars = string.ascii_letters + string.digits + '!@#$%¨&*()_-+={}[].,<>\/?|"^~§ªº°ç'
baralhar = random.SystemRandom()

print(''.join(baralhar.choice(chars) for i in range(tamanho)))
