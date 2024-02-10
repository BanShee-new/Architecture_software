# Архитектура ПО

## Урок 1. Введение в понятие архитектуры, проектирование ПО и жизненный цикл программного продукта. UML-диаграммы

### Задание 1. На основе Диаграмы классов ModelElements, разработать классы: Model Store, PoligonalModel (Texture, Poligon), Flash, Camera, Scene (Реализовать диограмму на любом языке программирования)

### Задание 2. Ознакомиться с документацией в свободном формате, которая может пригодиться Вам для дальнейшей работы:

ГОСТ Р ИСО/МЭК 12207-2010 Информационная технология (ИТ). Системная и программная инженерия. Процессы жизненного цикла программных средств.
ISO/IEC/IEEE 29148:2018 Systems and software engineering — Life cycle processes — Requirements engineering
Стандарты ЕСКД — единая система конструкторской документации
ГОСТ 2.001-2013 ЕСКД. Общие положения
Стандарты АСУ ГОСТ 34 — автоматизированные системы управления
Стандарты ЕСПД ГОСТ 19 — единая система программной документации

https://www.cybermedian.com/ru/a-comprehensive-guide-to-uml-class-diagram/

В этой призентации, в конце есть диограмма для Задания 1:

https://docs.google.com/presentation/d/1d-ReTu3A_944hmccTxqbUrRNMHtIDViiCMKvUUaKu24/edit?pli=1#slide=id.g161fe117232_1_7

### Задание 3. (На выбор 1 или 3 задание )
Создать UML Диограмму Классов..

** Задание: Разработка системы для онлайн-магазина книг. **
Описание:
Вы разрабатываете диаграмму классов для онлайн-магазина книг. Система позволяет пользователям просматривать каталог книг, оформлять заказы и получать информацию о заказанных книгах.

** Требования: **
Создайте классы для представления книг, пользователей и заказов.

Класс "Книга" должен содержать атрибуты, такие как название, автор, жанр и цена.

Примеры атрибутов:

> title: String (название книги)
> author: String (автор книги)
> genre: String (жанр книги)
> price: double (цена книги)

Класс "Пользователь" должен содержать атрибуты, такие как имя, адрес электронной почты и список заказанных книг.

Примеры атрибутов:

> name: String (имя пользователя)
> email: String (адрес электронной почты пользователя)
> orderedBooks: List<Book> (список заказанных книг)

Класс "Заказ" должен содержать атрибуты, такие как идентификатор заказа, дата оформления заказа и список книг, включенных в заказ.

Примеры атрибутов:

> orderId: int (идентификатор заказа)
> orderDate: Date (дата оформления заказа)
> orderedBooks: List<Book> (список книг в заказе)

Предоставьте методы в соответствующих классах для получения и установки значений атрибутов.

Примеры методов:

> public String getTitle(): возвращает название книги.
> public void setTitle(String title): устанавливает название книги.
> public List<Book> getOrderedBooks(): возвращает список заказанных книг пользователя.
> public void addBookToOrder(Book book): добавляет книгу в список заказанных книг.

Добавьте методы в класс "Пользователь" для добавления книг в список заказов и получения общей стоимости заказа.

Примеры методов:

> public double getTotalOrderCost(): возвращает общую стоимость заказа пользователя.

Добавьте метод в класс "Заказ" для получения информации о заказанных книгах и общей стоимости заказа.

Примеры методов:

> public List<Book> getOrderedBooks(): возвращает список книг в заказе.
> public double getTotalOrderCost(): возвращает общую стоимость заказа.

Предоставьте ассоциации между классами "Книга" и "Пользователь", а также между классами "Пользователь" и "Заказ".

Примеры ассоциаций:

"Пользователь" ассоциирован с "Книгой" через атрибут "orderedBooks" (отношение "1..").
"Пользователь" ассоциирован с "Заказом" через атрибут "orderedBooks" (отношение "1..").

Добавьте несколько методов в класс "Книга" и "Пользователь", чтобы сделать систему более интересной.

Примеры дополнительных методов:

> public void addToFavorites(Book book): добавляет книгу в избранное пользователя.
> public List<Order> getOrderHistory(): возвращает историю заказов пользователя.

Помните о правильных связях между классами, таких как агрегация или ассоциация.

** Ниже помощь для 3-го задания: **

Декомпозиция задачи на разработку диаграммы классов для онлайн-магазина книг:
Определение основных классов и их атрибутов:

Класс "Книга" с атрибутами: название, автор, жанр, цена.
Класс "Пользователь" с атрибутами: имя, адрес электронной почты, список заказанных книг.
Класс "Заказ" с атрибутами: идентификатор заказа, дата оформления заказа, список книг в заказе.
Определение связей между классами:

Класс "Пользователь" ассоциирован с классом "Книга" через атрибут "orderedBooks" (отношение "1..").
Класс "Пользователь" ассоциирован с классом "Заказ" через атрибут "orderedBooks" (отношение "1..").
Добавление методов в класс "Книга":

getTitle(): возвращает название книги.
setTitle(String title): устанавливает название книги.
getAuthor(): возвращает автора книги.
setAuthor(String author): устанавливает автора книги.
getGenre(): возвращает жанр книги.
setGenre(String genre): устанавливает жанр книги.
getPrice(): возвращает цену книги.
setPrice(double price): устанавливает цену книги.
Добавление методов в класс "Пользователь":

getName(): возвращает имя пользователя.
setName(String name): устанавливает имя пользователя.
getEmail(): возвращает адрес электронной почты пользователя.
setEmail(String email): устанавливает адрес электронной почты пользователя.
getOrderedBooks(): возвращает список заказанных книг пользователя.
addBookToOrder(Book book): добавляет книгу в список заказанных книг.
Добавление методов в класс "Заказ":

getOrderId(): возвращает идентификатор заказа.
setOrderId(int orderId): устанавливает идентификатор заказа.
getOrderDate(): возвращает дату оформления заказа.
setOrderDate(Date orderDate): устанавливает дату оформления заказа.
getOrderedBooks(): возвращает список книг в заказе.
addBookToOrder(Book book): добавляет книгу в список книг в заказе.
Добавление дополнительных методов (опционально):

addToFavorites(Book book): добавляет книгу в избранное пользователя.
getTotalOrderCost(): возвращает общую стоимость заказа пользователя.
getOrderHistory(): возвращает историю заказов пользователя.

## Урок 2. Объектно-ориентированные паттерны ##

Код с семинара на Java: https://github.com/vyntyk/FabricMethod.git

Код с семинара на Python: https://github.com/JuliaRyzhova/Software_architecture/tree/main/Seminar_2

### Задание ###

Прислать простую реализацию 5-ти Патернов, на любом языке, из списка:

Строитель (Builder)
Цепочка обязанностей (Chain of Responsibility)
Команда (Command)
Итератор (Iterator)
Посредник (Mediator)
Памятка (Memento)
Состояние (State)
Стратегия (Strategy)
Шаблонный метод (Template Method)
Посетитель (Visitor)

Познакомиться с другими типами паттернов(по желанию)

## Урок 3. Принципы SOLID ##

https://github.com/vyntyk/Solid.git

Продолжить работу с семинара.
рассмотрим четвертый принцип SOLID - Принцип сегрегации интерфейса (Interface Segregation Principle, ISP). Он гласит: "Клиенты не должны зависеть от интерфейсов, которые они не используют".
Вам надо написать код который исправяет эту ошибку и реализует этот принцип
Пример кода, который нарушает ISP:

> public interface Worker {
> void work();
> void eat();
> }

> public class HumanWorker implements Worker {
> public void work() {
> System.out.println("Человек работает");
> }

> public void eat() {
>    System.out.println("Человек ест");
>}
>}

> public class RobotWorker implements Worker {
> public void work() {
> System.out.println("Робот работает");
> }

> public void eat() {
>    throw new UnsupportedOperationException("Роботы не едят!");
> }
> }

> public class Main {
> public static void main(String[] args) {
> Worker worker = new RobotWorker();
> worker.work();
> worker.eat(); // Здесь возникнет исключение UnsupportedOperationException
> }
> }
> 
В этом примере класс RobotWorker не использует и не должен использовать метод eat(), поэтому он нарушает принцип сегрегации интерфейса.

И аналогично 5-ый принцип

Принцип инверсии зависимостей (Dependency Inversion Principle, DIP) гласит: "Зависимости на абстракциях. Нет зависимостей на что-то конкретное". Это означает, что высокоуровневые модули, которые обеспечивают сложную логику, должны быть независимы от низкоуровневых модулей, которые обеспечивают утилитарные функции. Оба типа модулей должны зависеть от абстракций.

Пример кода, который нарушает DIP:

> public class Text {
>     String text;
>
>     public Text(String text) {
>         this.text = text;
>     }
>
>     public String getText() {
>         return text;
>     }
> }
> 
> public class Printer {
>     public void print(Text text) {
>         System.out.println(text.getText());
>     }
> }
> 
> public class Main {
>     public static void main(String[] args) {
>         Text myText = new Text("Hello, world!");
>         Printer myPrinter = new Printer();
>         myPrinter.print(myText);
>     }
> }

В этом примере класс Printer зависит от конкретного класса Text.

## Урок 4. Компоненты. Принципы связности и сочетаемости компонентов ##

Вам необходимо доработать код, добавив контракты к методам, документацию и обеспечив высокую связанность и низкую сочетаемость:

> // Класс для геометрических фигур
> abstract class Shape {
>     // Общие поля и методы для всех геометрических фигур
>     abstract double getArea();
>     abstract double getPerimeter();
> }
> 
> // Класс для круга
> class Circle extends Shape {
>     private double radius;
> 
>     public Circle(double radius) {
>         this.radius = radius;
>     }
> 
>     @Override
>     double getArea() {
>         return Math.PI * radius * radius;
>     }
> 
>     @Override
>     double getPerimeter() {
>         return 2 * Math.PI * radius;
>     }
> }
> 
> // Класс для прямоугольника
> class Rectangle extends Shape {
>     private double length;
>     private double width;
> 
>     public Rectangle(double length, double width) {
>         this.length = length;
>         this.width = width;
>     }
> 
>     @Override
>     double getArea() {
>         return length * width;
>     }
> 
>     @Override
>     double getPerimeter() {
>         return 2 * (length + width);
>     }
> }
> 
> // Класс для треугольника
> class Triangle extends Shape {
>     private double side1;
>     private double side2;
>     private double side3;
> 
>     public Triangle(double side1, double side2, double side3) {
>         this.side1 = side1;
>         this.side2 = side2;
>         this.side3 = side3;
>     }
> 
>     @Override
>     double getArea() {
>         double s = (side1 + side2 + side3) / 2;
>         return Math.sqrt(s * (s - side1) * (s - side2) * (s - side3));
>     }
> 
>     @Override
>     double getPerimeter() {
>         return side1 + side2 + side3;
>     }
> }
> 
> // Главный класс приложения
> public class GeometryApp {
>     public static void main(String[] args) {
>         // Пример использования конкретных классов геометрических фигур
>         Circle circle = new Circle(5.0);
>         System.out.println("Площадь круга: " + circle.getArea());
>         System.out.println("Периметр круга: " + circle.getPerimeter());
> 
>         Rectangle rectangle = new Rectangle(4.0, 6.0);
>         System.out.println("Площадь прямоугольника: " + rectangle.getArea());
>         System.out.println("Периметр прямоугольника: " + rectangle.getPerimeter());
> 
>         Triangle triangle = new Triangle(3.0, 4.0, 5.0);
>        System.out.println("Площадь треугольника: " + triangle.getArea());
>         System.out.println("Периметр треугольника: " + triangle.getPerimeter());
>     }
> }

## Урок 5. Горизонтальные уровни и вертикальные срезы архитектуры ##

Джава: https://github.com/vyntyk/Srezy.git
Питон: https://github.com/JuliaRyzhova/Software_architecture/tree/main/Seminar_5

Реализовать любой паттерн с лекции . Выпустить диаграмму компонент UML по нему.

## Урок 6. Принципы построения приложений «чистая архитектура» ##

** Задание: Переделка программы под чистую архитектуру **

Вам предоставляется программа, которая представляет интернет-магазин книг с использованием коллекций. Ваша задача - переработать эту программу, применяя принципы чистой архитектуры для лучшей организации кода и разделения компонентов. В результате переработки программа должна следовать принципам Boundary-Control-Entity (BCE).

** Требования: **

- Создайте пакеты domain, data, и presentation.
- В пакете domain создайте классы, представляющие бизнес-объекты интернет-магазина книг. Например, Book - представляющий модель книги.
- В пакете data создайте интерфейс BookRepository, определяющий методы для управления книгами в интернет-магазине. Затем реализуйте этот интерфейс в классе InMemoryBookRepository, используя коллекции для хранения данных о книгах.
- В пакете presentation создайте класс Main, который будет представлять точку входа в приложение и обрабатывать пользовательские запросы.
- Используйте принципы чистой архитектуры для организации компонентов (BCE). Каждый компонент должен быть отделен от других, взаимодействие должно происходить через абстракции, а не через конкретные реализации.
- Перенесите функциональность работы с коллекциями и хранения данных в пакет data, таким образом, чтобы она не проникала в другие компоненты.
- Обеспечьте возможность добавления, удаления и получения списка книг через интерфейс BookRepository, а затем используйте его в Main для управления книгами.
- Убедитесь, что код программы чистый, читаемый и хорошо структурированный. Обеспечьте надлежащее разделение ответственности между компонентами и минимизируйте повторяющийся код.

** Примечание: **
Данный код предоставлен только для ознакомления с исходной реализацией и не представляет полный функционал интернет-магазина книг. Ваша задача - переработать его согласно принципам чистой архитектуры и обеспечить соответствующий функционал.

Вот пример кода, представляющего интернет-магазин книг с использованием коллекций, но без реализации чистой архитектуры:

> import java.util.ArrayList;
> import java.util.List;
> 
> // Класс представляющий книгу
> class Book {
>     private String id;
>     private String title;
>     private String author;
>     private double price;
> 
>     // Конструктор, геттеры и сеттеры
> }
> 
> // Класс, реализующий хранилище книг с использованием коллекций
> class BookStore {
>     private List<Book> books;
> 
>     public BookStore() {
>         books = new ArrayList<>();
>     }
> 
>     public void addBook(Book book) {
>         books.add(book);
>     }
> 
>     public void removeBook(Book book) {
>         books.remove(book);
>     }
> 
>     public List<Book> getAllBooks() {
>         return books;
>     }
> }
> 
> public class Main {
>     public static void main(String[] args) {
>         BookStore bookStore = new BookStore();
> 
>         // Добавляем книги в магазин
>         Book book1 = new Book("1", "Clean Code", "Robert C. Martin", 34.99);
>         Book book2 = new Book("2", "Effective Java", "Joshua Bloch", 29.99);
>         bookStore.addBook(book1);
>         bookStore.addBook(book2);
> 
>         // Получаем список всех книг в магазине
>         List<Book> allBooks = bookStore.getAllBooks();
>         for (Book book : allBooks) {
>             System.out.println("Книга: " + book.getTitle() + ", Автор: " + book.getAuthor() + ", Цена: $" + book.getPrice());
>         }
>     }
> }
