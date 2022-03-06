# pip install -r requirements.txt

from whatsapp import WhatsAppSender


def file_reader(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.read().splitlines():
            data.append(line)
    return data


if __name__ == "__main__":
    print("Start. Слава Україні!")

    numbers_file = 'numbers.txt'
    message_file = 'message.txt'

    numbers = file_reader(numbers_file)
    message = ' '.join(file_reader(message_file))

    if len(numbers) < 1:
        print('Add phone numbers to numbers.txt')
    elif len(message) < 1:
        print('Add your message to message.txt')
    else:
        whatsapp = WhatsAppSender()
        whatsapp.worker(numbers, message, timeout=7)
        print('Done. Героям слава!')
