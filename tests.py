import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_added_book_has_no_genre(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'

        collector.add_new_book(name)
        
        assert name in collector.books_genre
        assert collector.books_genre[name] == ''

    def test_set_book_genre_success(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        genre = 'Ужасы'

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    def test_get_book_genre_success(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        genre = 'Ужасы'

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre
    
    @pytest.mark.parametrize('books, expected_result', [
        ({'Гордость и предубеждение и зомби': 'Ужасы'}, 
         ['Гордость и предубеждение и зомби']),

        ({'Гордость и предубеждение и зомби': 'Ужасы', 
          'Что делать, если ваш кот хочет вас убить': 'Комедии',
          'Приключения Шерлока Холмса': 'Детективы'}, 
          ['Гордость и предубеждение и зомби']),
          
        ({'Что делать, если ваш кот хочет вас убить': 'Комедии',
          'Приключения Шерлока Холмса': 'Детективы'}, []),
          
        ({'Гордость и предубеждение и зомби': 'Ужасы',
          'Оно': 'Ужасы',
          'Приключения Шерлока Холмса': 'Детективы'},
          ['Гордость и предубеждение и зомби', 'Оно'])])
    def test_get_books_with_specific_genre_returns_correct_books(self, books, expected_result):
        collector = BooksCollector()
        
        for name, genre in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre) 
        
        
        result = collector.get_books_with_specific_genre('Ужасы')  
        assert expected_result == result
 
    @pytest.mark.parametrize('books, expected_result', 
    [({'Гордость и предубеждение и зомби': 'Ужасы'},
      {'Гордость и предубеждение и зомби': 'Ужасы'}),
     
     ({'Гордость и предубеждение и зомби': 'Ужасы', 
      'Что делать, если ваш кот хочет вас убить': 'Комедии', 
      'Приключения Шерлока Холмса': 'Детективы'},
      {'Гордость и предубеждение и зомби': 'Ужасы', 
      'Что делать, если ваш кот хочет вас убить': 'Комедии', 
      'Приключения Шерлока Холмса': 'Детективы'})])
    def test_get_books_genre_with_various_collections(self, books, expected_result):
        collector = BooksCollector()

        for name, genre in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre) 

        result = collector.get_books_genre()
        assert result == expected_result

    @pytest.mark.parametrize('books, expected_result', 
        [({'Что делать, если ваш кот хочет вас убить': 'Комедии'}, 
          ['Что делать, если ваш кот хочет вас убить']),

         ({'Гордость и предубеждение и зомби': 'Ужасы', 
          'Что делать, если ваш кот хочет вас убить': 'Комедии',
          'Приключения Шерлока Холмса': 'Детективы'}, 
          ['Что делать, если ваш кот хочет вас убить']),
          
         ({'Гордость и предубеждение и зомби': 'Ужасы',
           'Приключения Шерлока Холмса': 'Детективы'}, []),
           
         ({'Незнайка на Луне': 'Мультфильмы', 
           'Что делать, если ваш кот хочет вас убить': 'Комедии',
           'Приключения Шерлока Холмса': 'Детективы' }, 
          ['Незнайка на Луне', 'Что делать, если ваш кот хочет вас убить'])])
    def test_get_books_for_children_returns_correct_books(self, books, expected_result):
        collector = BooksCollector()

        for name, genre in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)


        result = collector.get_books_for_children()

        assert result == expected_result

    def test_add_book_in_favorites_book_added(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'

        collector.add_new_book(name)

        collector.add_book_in_favorites(name)

        assert name in collector.favorites

    def test_add_book_in_favorites_cant_add_again(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'

        collector.add_new_book(name)
        collector.add_book_in_favorites(name)

        initial_length = len(collector.favorites)
        
        collector.add_book_in_favorites(name)

        assert initial_length == len(collector.favorites)

    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'

        collector.add_new_book(name)
        collector.add_book_in_favorites(name)

        collector.delete_book_from_favorites(name)

        assert not name in collector.favorites
   
    def test_get_list_of_favorites_books_one_book_added(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'

        collector.add_new_book(name)
        collector.add_book_in_favorites(name)

        result = collector.get_list_of_favorites_books()

        assert result == [name]
