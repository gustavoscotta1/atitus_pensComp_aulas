def get_questions(amount: int = 10, difficulty: str = 'easy') -> dict:
    import http.client
    import json

    conn = http.client.HTTPSConnection("opentdb.com")
    conn.request("GET", f"/api.php?amount={amount}&difficulty={difficulty}&type=multiple")
    response = conn.getresponse()
    response_text = response.read().decode()
    conn.close()
    return json.loads(response_text)


def parse_text(html_string: str) -> str:
    import html

    # Convert HTML entity to regular single quote
    return html.unescape(html_string)


def start_quiz():
    questions_data = get_questions()
    questions = questions_data.get("results", [])

    score = 0
    for i, q in enumerate(questions, 1):
        question = parse_text(q["question"])
        correct_answer = parse_text(q["correct_answer"])
        options = [parse_text(opt) for opt in q["incorrect_answers"]] + [correct_answer]
        options.sort()

        print(f"Pergunta {i}: {question}")
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")

        resposta = input("Digite o número da resposta correta: ")
        try:
            resposta_idx = int(resposta) - 1
            if options[resposta_idx] == correct_answer:
                print("Resposta correta!\n")
                score += 1
            else:
                print(f"Errado! A resposta correta era: {correct_answer}\n")
        except (ValueError, IndexError):
            print(f"Resposta inválida! A resposta correta era: {correct_answer}\n")

    print(f"Quiz finalizado! Você acertou {score} de {len(questions)} perguntas.")


start_quiz()

