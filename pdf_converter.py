import PyPDF2


def get_html_content(highlighted_text):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Your HTML Page</title>
    </head>
    <body>
        <p>{highlighted_text}</p>
    </body>
    </html>
    """
    return html_content

def extract_text_from_pdf(pdf_file_path, output_text_file):
    # PDF 파일 열기
    pdf_file = open(pdf_file_path, 'rb')

    # PDF 리더 객체 생성
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # 텍스트 추출
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    # 텍스트를 .txt 파일로 저장
    with open(output_text_file, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)

    # 파일 닫기
    pdf_file.close()
    
def highlight_words(text_content, highlight_word):
    highlighted_text = text_content.replace(highlight_word, f"<span style='background-color: yellow;'>{highlight_word}</span>")
    return highlighted_text

def text_to_html(text_file, html_file, highlight_word):
    with open("output2.txt", "r") as text_file:
        text_content = text_file.read()
    # 특정 단어를 찾아 하이라이트 처리
    highlighted_text = highlight_words(text_content, highlight_word)
    # HTML 문서 작성
    html_content = get_html_content(highlighted_text)
    # HTML 파일로 저장
    with open("output.html", "w") as html_file:
        html_file.write(html_content)


if __name__ == "__main__":
    pdf_file_path = '보고서1.pdf'  # PDF 파일 경로를 적절히 변경하세요.
    text_file = 'output.txt'  # 출력 텍스트 파일 경로를 적절히 변경하세요.
    html_file = "output.html"
    
    # 하이라이트할 단어
    highlight_word = "아이다"
    extract_text_from_pdf(pdf_file_path, text_file)
    text_to_html(text_file, html_file)