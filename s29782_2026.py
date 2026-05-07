import random
from collections import defaultdict

def generate_sequence(length: int) -> str:
    """Zwraca losową sekwencję DNA o zadanej długości."""
    nucleotides = ['A', 'C', 'G', 'T']
    return "".join(random.choice(nucleotides) for _ in range(length))

def calculate_stats(sequence: str) -> dict:
    """Zwraca słownik ze statystykami sekwencji.
    Klucze: "A", "C", "G", "T" (wartości float, %),
           "GC" (wartość float, %)."""
    stats=defaultdict(float)
    length=len(sequence)
    for n in sequence:
        stats[n]+=1
        if n=="G" or n=="C":
            stats["GC"]+=1

    

    for k in stats.keys():
        stats[k]=stats[k]/length

    return stats

    
    

def insert_name(sequence: str, name: str) -> str:
    """Wstawia imię w losową pozycję sekwencji.
    Imię zapisane małymi literami."""
    idx = random.randint(0, len(sequence))
    return sequence[:idx] + name.lower() + sequence[idx:]

def format_fasta(seq_id: str, description: str,
                 sequence: str, line_width: int = 80) -> str:
    """Zwraca sformatowany rekord FASTA jako string."""
    header = f">{seq_id} {description}".strip()
    
    lines = [header]
    for i in range(0, len(sequence), line_width):
        lines.append(sequence[i:i + line_width])
    
    return "\n".join(lines)


def validate_positive_int(prompt: str,
                          min_val: int = 1,
                          max_val: int = 100_000) -> int:
    """Pobiera od użytkownika liczbę całkowitą z zakresu.
    W przypadku błędu powtarza pytanie."""
    while True:
        try:
            length=int(input(prompt))
            if 1 <= length <= 100000:
              return length
            else:
                print("Błąd: wartość musi być liczbą całkowitą z zakresu [1, 100000].")
        except ValueError: 
            print("Błąd: wartość musi być liczbą całkowitą z zakresu [1, 100000].")

def get_ID()->str:
    id=input("Podaj ID sekwencji: ")
    return id

def save_to_fasta(seq_id: str,fasta:str):
    filename = f"{seq_id}.fasta" 
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(fasta)
        print(f"\nSukces! Sekwencja została zapisana w pliku: {filename}")
    except IOError as e:
        print(f"Błąd zapisu pliku: {e}")

def pretty_print_stats(stats :dict):
    print(f"A: {round(stats["A"]*100,3)}%")
    print(f"C: {round(stats["C"]*100,3)}%")
    print(f"G: {round(stats["G"]*100,3)}%")
    print(f"T: {round(stats["T"]*100,3)}%")
    print(f"\nGC-content: {round(stats["GC"]*100,3)}%")








def main():
    seq_len=validate_positive_int("Podaj długość sekwencji: ")
    seq_id=get_ID()
    seq=generate_sequence(seq_len)
    seq_w_name=insert_name(seq,input("Podaj imie: "))
    print(format_fasta(seq_id,"bez",seq_w_name))
    save_to_fasta(seq_id,format_fasta(seq_id,"bez",seq_w_name))
    stats=calculate_stats(seq)
    pretty_print_stats(stats)


   
   

if __name__ == "__main__":
    main()