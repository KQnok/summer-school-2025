prob_history = 0.1
prob_charms = 0.25
prob_call = 0.5

history_books = 5
charm_books = 2
call_books = 3

all_books = 10

result_baza = (history_books/all_books * prob_history +
               charm_books/all_books * prob_charms +
               call_books/all_books * prob_call)

print(f'Вероятность повреждения одной случайной книги из известной выдачи = {result_baza:.3f}')

prob_get_book = 1/3

book_is_not_damaged = (prob_get_book * (1 - prob_history) +
                       prob_get_book * (1 - prob_charms) +
                       prob_get_book * (1 - prob_call))

result_pro = 1 - (book_is_not_damaged)**all_books

print(f'Вероятность хотя бы одной повреждённой среди 10 книг, выданных "вслепую" = {result_pro:.3f}')