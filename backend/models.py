from django.db import models


# Create your models here.

# create table borrower
# (
#     borrower_id     int primary key,
#     borrower_name   varchar(10) not null unique,
#     borrower_pwd    varchar(15) not null,
#     borrower_phone  char(10)    not null,
#     borrower_credit smallint default 0
# );

class Borrower(models.Model):
    borrower_id = models.AutoField(primary_key=True)
    borrower_name = models.CharField(max_length=10, null=False, unique=True)
    borrower_pwd = models.CharField(max_length=15, null=False)
    borrower_phone = models.CharField(max_length=10, null=False)
    borrower_credit = models.SmallIntegerField(default=0)


# create table manager
# (
#     manager_id    int primary key,
#     manager_name  varchar(10) not null unique,
#     manager_pwd   varchar(15) not null,
#     manager_phone char(10)    not null
# );

class Manager(models.Model):
    manager_id = models.AutoField(primary_key=True)
    manager_name = models.CharField(max_length=10, null=False, unique=True)
    manager_pwd = models.CharField(max_length=15, null=False)
    manager_phone = models.CharField(max_length=10, null=False)


# create table book
# (
#     book_id           int primary key,
#     book_name         varchar(30) not null,
#     book_writer       varchar(30)  default 'unknown',
#     book_introduction varchar(300) default 'nothing',
#     book_hot          smallint     default 0,
#     book_path         varchar(50)  default '/default.img'
# );

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=30, null=False)
    book_writer = models.CharField(max_length=30, default="unknown")
    book_introduction = models.CharField(max_length=300, default="nothing")
    book_hot = models.SmallIntegerField(default=0)
    book_path = models.CharField(max_length=50, default="/default.img")
    status_choices = (
        (0, "可借阅"),
        (1, "不可借阅"),
    )
    status = models.SmallIntegerField(choices=status_choices)


# create table review
# (
#     review_id      int primary key,
#     review_book    int,
#     review_content varchar(300) not null,
#     review_mark    smallint     not null,
#     foreign key (review_book) references book (book_id)
# );

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    review_book = models.ForeignKey(to="Book", to_field="book_id", on_delete=models.CASCADE)
    review_content = models.CharField(max_length=300, null=False)
    review_mark = models.SmallIntegerField(null=False)


# CREATE TABLE Topic
# (
#     topic_id    INT PRIMARY KEY,
#     topic_title VARCHAR(30) NOT NULL,
#     topic_intro VARCHAR(300)
# );

class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    topic_title = models.CharField(max_length=30, null=False)
    topic_intro = models.CharField(max_length=300)


# CREATE TABLE Message
# (
#     message_id      INT PRIMARY KEY,
#     message_writer  INT,
#     message_content VARCHAR(30) NOT NULL,
#     message_topic   INT,
#     message_reply   INT,
#     FOREIGN KEY (message_writer) REFERENCES Borrower (borrower_id),
#     FOREIGN KEY (message_topic) REFERENCES Topic (topic_id),
#     FOREIGN KEY (message_reply) REFERENCES Message (message_id)
# );

class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    message_writer = models.ForeignKey(to="Borrower", to_field="borrower_id", on_delete=models.CASCADE)
    message_content = models.CharField(max_length=30, null=False)
    message_topic = models.ForeignKey(to="Topic", to_field="topic_id", on_delete=models.CASCADE)
    message_reply = models.ForeignKey(to="Message", to_field="message_id", on_delete=models.CASCADE)


# CREATE TABLE Borrow_record
# (
#     borrower_id INT ,
#     book_id     INT ,
#     borrow_time DATETIME NOT NULL,
#     return_time DATETIME NOT NULL,
#     FOREIGN KEY (borrower_id) REFERENCES borrower (borrower_id),
#     FOREIGN KEY (book_id) REFERENCES book (book_id)
# );

class Borrow_record(models.Model):
    borrower_id = models.ForeignKey(to="Borrower", to_field="borrower_id", on_delete=models.CASCADE)
    book_id = models.ForeignKey(to="Book", to_field="book_id", on_delete=models.CASCADE)
    borrow_time = models.DateTimeField(null=False)
    return_time = models.DateTimeField(null=False)

# CREATE TABLE entry_record
# (
#     manager_id INT,
#     book_id    INT,
#     time       DATETIME NOT NULL,
#     FOREIGN KEY (manager_id) REFERENCES manager (manager_id),
#     FOREIGN KEY (book_id) REFERENCES book (book_id)
#
# );

class Entry_record(models.Model):
    manager_id = models.ForeignKey(to="Manager", to_field="manager_id", on_delete=models.CASCADE)
    book_id = models.ForeignKey(to="Book", to_field="book_id", on_delete=models.CASCADE)
    time = models.DateTimeField(null=False)

# CREATE TABLE default_record
# (
#     borrower_id INT ,
#     book_id     INT ,
#     return_time DATETIME NOT NULL,
#     FOREIGN KEY (borrower_id) references borrower (borrower_id),
#     FOREIGN KEY (book_id) references book (book_id)
# );

class Default_record(models.Model):
    borrower_id = models.ForeignKey(to="Borrower", to_field="borrower_id", on_delete=models.CASCADE)
    book_id = models.ForeignKey(to="Book", to_field="book_id", on_delete=models.CASCADE)
    return_time = models.DateTimeField(null=False)


class Borrower_book(models.Model):
    borrower_id = models.ForeignKey(to="Borrower", to_field="borrower_id", on_delete=models.CASCADE)
    book_id = models.ForeignKey(to="Book", to_field="book_id", on_delete=models.CASCADE)