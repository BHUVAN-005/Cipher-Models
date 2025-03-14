from flask import Flask, render_template, request

app = Flask(__name__)

# Caesar Cipher Logic
def caesar_cipher(text, shift, mode):
    result = []
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            shifted = ord(char) + shift_amount
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result.append(chr(shifted))
        else:
            result.append(char)
    return ''.join(result)

# Vigenère Cipher Logic
def vigenere_cipher(text, keyword, mode):
    keyword = (keyword * (len(text) // len(keyword) + 1))[:len(text)]
    result = []
    for i in range(len(text)):
        char = text[i]
        key = keyword[i].lower()
        if char.isalpha():
            shift = ord(key) - ord('a')
            if mode == 'decrypt':
                shift = -shift
            if char.islower():
                shifted = ord(char) + shift
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                shifted = ord(char) + shift
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result.append(chr(shifted))
        else:
            result.append(char)
    return ''.join(result)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def index_2():
    return render_template('index.html')


# Caesar Cipher route
@app.route('/caesar.html', methods=['GET', 'POST'])
def caesar():
    cipher_text = ""
    if request.method == 'POST':
        text = request.form['input_text']
        shift = int(request.form['shift'])
        mode = request.form['mode']
        cipher_text = caesar_cipher(text, shift, mode)
    return render_template('caesar.html', cipher_text=cipher_text)

# Vigenère Cipher route
@app.route('/vigenere.html', methods=['GET', 'POST'])
def vigenere():
    cipher_text = ""
    if request.method == 'POST':
        text = request.form['input_text']
        keyword = request.form['keyword']
        mode = request.form['mode']
        cipher_text = vigenere_cipher(text, keyword, mode)
    return render_template('vigenere.html', cipher_text=cipher_text)

@app.route('/dev.html')
def dev():
    return render_template('dev.html')

if __name__ == "__main__":
    app.run(debug=True)
