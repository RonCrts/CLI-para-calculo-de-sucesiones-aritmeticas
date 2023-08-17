import numpy as np
from numba import float64, int64, prange
from numba.experimental import jitclass
import time
from rich.console import Console
from rich.text import Text
from rich.style import Style
import click

spec = [
    ('n', int64),
    ('a1', float64),
    ('d', float64),
    ('sequence', float64[:])
]

@jitclass(spec)
class ArithmeticSequence:
    def __init__(self, n, a1, d):
        self.n = n
        self.a1 = a1
        self.d = d
        self.sequence = np.zeros(n, dtype=np.float64)
        try:
            for i in prange(n):
                self.sequence[i] = a1 + d*i
        except:
            return None

    def is_arithmetic(self):
        for i in prange(2, self.n):
            if self.sequence[i] - self.sequence[i-1] != self.d:
                return False
        return True

    def is_ascending(self):
        for i in prange(1, self.n):
            if self.sequence[i] <= self.sequence[i-1]:
                return False
        return True

    def is_descending(self):
        for i in prange(1, self.n):
            if self.sequence[i] >= self.sequence[i-1]:
                return False
        return True

    def nth_term(self, n):
        if self.n < n:
            sequence = ArithmeticSequence(n, self.a1, self.d)
            return sequence.sequence[n-1]
        else:
            return self.sequence[n-1]

    def sum_of_terms(self):
        return self.n*(self.a1 + self.d*(self.n-1))/2


class SequenceInfoBuilder:
    def __init__(self):
        self.sequence = None
        self.console = Console()

    def set_sequence(self, n, a1, d):
        try:
            self.sequence = ArithmeticSequence(n, a1, d)
        except Exception as e:
            self.console.print(Text(f"Error: {e}", style=Style(color='red')))
        return self

    def print_sequence(self):
        try:
            start_time = time.time()
            text = Text(f"Sequence: {self.sequence.sequence}", style=Style(color="green"))
            self.console.print(text)
            end_time = time.time()
            text = Text(f"Execution time: {end_time - start_time} seconds", style=Style(color="yellow"))
            self.console.print(text)
        except Exception as e:
            self.console.print(Text(f"Error: {e}", style=Style(color='red')))
        return self

    def print_is_arithmetic(self):
        try:
            start_time = time.time()
            text = Text(f"Is Arithmetic: {self.sequence.is_arithmetic()}", style=Style(color="green"))
            self.console.print(text)
            end_time = time.time()
            text = Text(f"Execution time: {end_time - start_time} seconds", style=Style(color="yellow"))
            self.console.print(text)
        except Exception as e:
            self.console.print(Text(f"Error: {e}", style=Style(color='red')))
        return self

    def print_is_ascending(self):
        try:
            start_time = time.time()
            text = Text(f"Is Ascending: {self.sequence.is_ascending()}", style=Style(color="green"))
            self.console.print(text)
            end_time = time.time()
            text = Text(f"Execution time: {end_time - start_time} seconds", style=Style(color="yellow"))
            self.console.print(text)
        except Exception as e:
            self.console.print(Text(f"Error: {e}", style=Style(color='red')))
        return self

    def print_is_descending(self):
        try:
            start_time = time.time()
            text = Text(f"Is Descending: {self.sequence.is_descending()}", style=Style(color="green"))
            self.console.print(text)
            end_time = time.time()
            text = Text(f"Execution time: {end_time - start_time} seconds", style=Style(color="yellow"))
            self.console.print(text)
        except Exception as e:
            self.console.print(Text(f"Error: {e}", style=Style(color='red')))
        return self

    def print_nth_term(self, n):
        try:
            start_time = time.time()
            text = Text(f"{n}th term: {self.sequence.nth_term(n)}", style=Style(color="green"))
            self.console.print(text)
            end_time = time.time()
            text = Text(f"Execution time: {end_time - start_time} seconds", style=Style(color="yellow"))
            self.console.print(text)
        except Exception as e:
            self.console.print(Text(f"Error: {e}", style=Style(color='red')))
        return self

    def print_sum_of_terms(self):
        try:
            start_time = time.time()
            text = Text(f"Sum of terms: {self.sequence.sum_of_terms()}", style=Style(color="green"))
            self.console.print(text)
            end_time = time.time()
            text = Text(f"Execution time: {end_time - start_time} seconds", style=Style(color="yellow"))
            self.console.print(text)
        except Exception as e:
            self.console.print(Text(f"Error: {e}", style=Style(color='red')))
        return self

@click.group()
def cli():
    pass

@cli.command()
@click.option('--n', type=int, required=True, help='Number of terms in the sequence')
@click.option('--a1', type=float, required=True, help='First term of the sequence')
@click.option('--d', type=float, required=True, help='Common difference of the sequence')
@click.option('--nth-term', type=int, help='Print the nth term of the sequence')

def set_sequence(n, a1, d, nth_term):
    builder = SequenceInfoBuilder()
    builder.set_sequence(n, a1, d)
    builder.print_sequence()
    builder.print_is_arithmetic()
    builder.print_is_ascending()
    builder.print_is_descending()
    builder.print_nth_term(nth_term)
    builder.print_sum_of_terms()

if __name__ == '__main__':
    cli()