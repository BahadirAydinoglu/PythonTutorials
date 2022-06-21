with open("Dosya_1.txt",encoding="UTF-8") as file:
    content = file.read()
    print(content)
    file.seek(0) # 0 değeri ile en başa gönderir, 
    print(file.tell()) # Cursorun son bulunduğu konumu verir


