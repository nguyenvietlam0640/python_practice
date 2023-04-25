
import psycopg2


class Human:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f'{self.name}(Human)'


class Student(Human):
    def __init__(self, name: str, math_score: float, literate_score: float, english_score: float, id=None) -> None:
        self.name = name
        self.id = id
        self.math_score = float(math_score)
        self.literate_score = float(literate_score)
        self.english_score = float(english_score)

    def __str__(self) -> str:
        return f'{self.name}(Student)'

    def is_valid(self):
        if not self.name:
            raise ValueError('name must be provided')

        if type(float(self.math_score)) != float:
            raise TypeError('math must be interger or float')

        if type(float(self.literate_score)) != float:
            raise TypeError('literate must be interger or float')

        if type(float(self.english_score)) != float:
            raise TypeError('english must be interger or float')

        return True

    def average_score(self) -> float:
        if self.is_valid():
            total = self.math_score+self.literate_score+self.english_score

            if not total:
                return 0

            return round(total/3, 2)

    def all() -> list:
        students_obj = []
        connect = psycopg2.connect(host='localhost', dbname='postgres',
                                   user='postgres', password='vietlam', port='5432')
        cur = connect.cursor()

        cur.execute("""SELECT * FROM student""")

        students = cur.fetchall()

        for student in students:
            student_obj = Student(
                name=student[1], math_score=student[2], literate_score=student[3], english_score=student[4], id=student[0])
            students_obj.append(student_obj)
        connect.commit()
        cur.close()
        connect.close()
        return students_obj

    def save(self):
        if self.is_valid():
            connect = psycopg2.connect(host='localhost', dbname='postgres',
                                       user='postgres', password='vietlam', port='5432')
            cur = connect.cursor()
            cur.execute("""SELECT id 
                        FROM student 
                        ORDER BY id DESC 
                        LIMIT 1""")

            new_id = cur.fetchone()[0]

            cur.execute("""CREATE TABLE IF NOT EXISTS student (
                            id INT PRIMARY KEY,
                            name VARCHAR(255),
                            math_score NUMERIC (4, 2),
                            literate_score NUMERIC (4, 2),
                            english_score NUMERIC (4, 2)
                        );
                        """)

            cur.execute(
                f"""INSERT INTO student (id,name, math_score, literate_score, english_score) VALUES 
                ({new_id+1},'{self.name}', {self.math_score}, {self.literate_score}, {self.english_score});""")
            connect.commit()
            cur.close()
            connect.close()

    def ascending_average_sort():
        leng = len(Student.all())

        if leng <= 1:
            return Student.all()
        sorted_student = Student.all()

        for i in range(leng-1):
            for j in range(i+1, leng):
                print(sorted_student[i].average_score(),
                      type(sorted_student[i].average_score()))
                if sorted_student[i].average_score() > sorted_student[j].average_score():
                    sorted_student[i], sorted_student[
                        j] = sorted_student[j], sorted_student[i]

        return sorted_student

    def decending_average_sort():
        leng = len(Student.all())

        if leng <= 1:
            return Student.all()
        sorted_student = Student.all()

        for i in range(leng-1):
            for j in range(i+1, leng):
                print(sorted_student[i].average_score(),
                      type(sorted_student[i].average_score()))
                if sorted_student[i].average_score() < sorted_student[j].average_score():
                    sorted_student[i], sorted_student[
                        j] = sorted_student[j], sorted_student[i]

        return sorted_student
