# lms.py

# Book class to handle Book objects

class Book:
	def __init__(self, title, author, first_release, number_of_page):
		self.title = title
		self.author = author
		self.first_release = first_release
		self.number_of_page = number_of_page
		

	
			
# Library fields and functions

class Library:
	def __init__(self):
		self.books_file = open("books.txt","a+")
	def build_list_of_books(self):
		self.books_file.seek(0)
		books_lines = self.books_file.read().splitlines()
		books_list = []
		for single_book_line in books_lines:
			title, author, first_release, number_of_page = single_book_line.split(",")
			single_book = Book(title, author, first_release, number_of_page)
			books_list.append(single_book)
		return books_list
		
	def find_index_of_book_with_title(self, lst, title):
		i = 0
		not_found = True
		while not_found and i < len(lst):
    			element = lst[i]
    			not_found = title != element.__dict__["title"]
    			i += 1
		if not_found:
			print('*** You provided unknown title of book to remove.')
			return -1
		else:
			return i-1
	def list_books(self):
		books_list = self.build_list_of_books()
		for i, single_book in enumerate(books_list):
			t, a, fr, np = single_book.__dict__.values()
			print("Book", i)
			print( "Title:", t, ",", "Author:", a)
	def add_book(self):
		while True:
			try:
				title = input("Please provide book title:")
				if not title:
					raise ValueError('Empty title')
				elif title.find(",") != -1:
					raise ValueError('Contains comma')
				else:
					break
			except ValueError as e:
	    			print(e)
		while True:
			try:
				author = input("Please provide book author:")
				if not author:
					raise ValueError('Empty author')
				elif author.find(",") != -1:
					raise ValueError('Contains comma')
				else:
					break
			except ValueError as e:
				print(e)
		while True:
			try:
				first_release = input("Please provide book first release:")
				if not first_release:
					raise ValueError('Empty first release')
				elif first_release.find(",") != -1:
					raise ValueError('Contains comma')				
				else:
					break			
			except ValueError as e:
				print(e)
		while True:
			try:
				number_of_page = input("Please provide book number of page:")
				if not number_of_page:
					raise ValueError('Empty number of page')
				elif number_of_page.find(",") != -1:
					raise ValueError('Contains comma')				
				else:
					break
			except ValueError as e:
	    			print(e)
		self.books_file.write(title + "," + author + "," + first_release + "," + number_of_page + "\n")
	
	def remove_book(self):
		books_list = self.build_list_of_books()
		while True:
			try:
				title = input("Please provide title of the book to remove:")
				if not title:
					raise ValueError('Empty title')
				else:
					break
			except ValueError as e:
	    			print(e) 
		index = self.find_index_of_book_with_title(books_list, title)
		if index != -1:
			del books_list[index]
			self.books_file.truncate(0)
			self.books_file.seek(0)
			for single_book in books_list:
				t, a, fr, np = single_book.__dict__.values()
				self.books_file.write(t + "," + a + "," + fr + "," + np + "\n")
			return index
		else:
			return -1
	def __del__(self):
        	self.books_file.close()
        	
# Defines main flow and user interaction
class Application:
	def __init__(self):
		self.lib = Library()
	
	def main(self):
		choice = "0"
		while choice != "q":
			print("*** MENU***")
			print("1) List Books")
			print("2) Add Book")
			print("3) Remove Book")
			print("q) Quit")
			choice = input("Kindly choose one of the above:") 
			if choice == "1":
				print("*** List of the books***")
				self.lib.list_books()
			elif choice == "2":
				self.lib.add_book()
				print("*** Book has been added succesfully.")
			elif choice == "3":
				removed_index  = self.lib.remove_book()
				print("*** Book at line:" + str(removed_index) +" has been removed succesfully.")
			elif choice == "q":
				print("*** You have choosen to quit the program.***")
				print("********************************************")
			else:
				print("*** You should choose exactly one of the menu items.")		


app = Application()
app.main()
