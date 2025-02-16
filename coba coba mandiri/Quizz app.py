import random
from typing import List, Dict

class PythonQuiz:
    def __init__(self):
        self.questions: List[Dict] = [
            {
                "question": "Apa output dari print(2 ** 3 ** 2)?",
                "options": ["64", "512", "SyntaxError", "81"],
                "correct": 1,
                "explanation": "Operator eksponen memiliki hak lebih tinggi dan dievaluasi dari kanan: 3**2=9 lalu 2**9=512"
            },
            {
                "question": "Manakah yang membuat dictionary kosong?",
                "options": ["{}", "dict()", "set()", "Kedua pertama benar"],
                "correct": 3,
                "explanation": "{} dan dict() sama-sama membuat dictionary kosong"
            },
            {
                "question": "Apa fungsi dari __init__ dalam class?",
                "options": [
                    "Menginisialisasi objek",
                    "Menghancurkan objek",
                    "Mengubah class parent",
                    "Mengembalikan string"
                ],
                "correct": 0,
                "explanation": "__init__ adalah constructor untuk inisialisasi objek"
            }
        ]
        self.score = 0
        self.skipped = 0

    def shuffle_options(self, question: Dict) -> List[str]:
        """Mengacak opsi jawaban dan mengembalikan indeks jawaban yang benar setelah diacak"""
        options = question["options"].copy()
        correct_answer = options[question["correct"]]
        random.shuffle(options)
        new_correct_index = options.index(correct_answer)
        return options, new_correct_index

    def validate_input(self, user_input: str) -> bool:
        """Validasi input pengguna"""
        return user_input.strip().lower() in ['a', 'b', 'c', 'd', 'skip']

    def display_question(self, question: Dict, q_num: int, total: int) -> None:
        """Menampilkan pertanyaan dengan format yang rapi"""
        print(f"\nPertanyaan {q_num}/{total}")
        print("=" * 50)
        print(question["question"] + "\n")
        
        options, correct_idx = self.shuffle_options(question)
        for i, option in enumerate(options):
            print(f"{chr(65 + i)}. {option}")
        
        print("\nMasukkan pilihan (A/B/C/D) atau ketik 'skip' untuk lewati")

    def run_quiz(self) -> None:
        """Menjalankan alur kuis utama"""
        random.shuffle(self.questions)
        total_questions = len(self.questions)

        for idx, question in enumerate(self.questions, 1):
            while True:
                self.display_question(question, idx, total_questions)
                user_input = input(">>> ").strip().lower()

                if not self.validate_input(user_input):
                    print("Input tidak valid! Gunakan A/B/C/D atau 'skip'")
                    continue
                
                if user_input == 'skip':
                    self.skipped += 1
                    print("Pertanyaan dilewati!\n" + "="*50)
                    break
                
                selected = ord(user_input) - 97
                options, correct_idx = self.shuffle_options(question)
                
                if selected == correct_idx:
                    self.score += 1
                    print("\n✅ Benar!")
                else:
                    print(f"\n❌ Salah! Jawaban benar: {chr(65 + correct_idx)}")
                
                print(f"Penjelasan: {question['explanation']}")
                print("=" * 50 + "\n")
                break

        self.show_results()

    def show_results(self) -> None:
        """Menampilkan hasil akhir"""
        print("\n" + "=" * 50)
        print("HASIL AKHIR".center(50))
        print("=" * 50)
        print(f"Total Pertanyaan: {len(self.questions)}")
        print(f"Jawaban Benar: {self.score}")
        print(f"Dilewati: {self.skipped}")
        print(f"Nilai Akhir: {(self.score/len(self.questions))*100:.1f}%")
        print("=" * 50)

if __name__ == "__main__":
    print("KUIS PEMROGRAMAN PYTHON".center(50, "="))
    print("Selamat datang! Jawab pertanyaan berikut:")
    print("(Anda bisa melewatkan pertanyaan dengan mengetik 'skip')\n")
    
    quiz = PythonQuiz()
    quiz.run_quiz()