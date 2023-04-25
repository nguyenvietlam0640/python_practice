import models


def show_list(students):
    print('--------------------------- STUDENT TABLE ---------------------------')
    for student in students:
        print(f'stt: {student.id+1}\t'
              f'name: {student.name}\t'
              f'math: {student.math_score}\t'
              f'literate: {student.literate_score}\t'
              f'english: {student.english_score}\t'
              f'average: {student.average_score()}'
              )
    print("---------------------------------------------------------------------")


if __name__ == '__main__':
    while True:

        print('type your number')

        print('1: to add\n'
              '2: to sort\n'
              '3: to show tabel\n'
              '4: to cancel')
        ans = input('your answer: ')

        if ans == '1':
            name = input('type name student: ')
            math = input('type math score: ')
            literate = input('type literate score: ')
            english = input('type english score: ')

            student = models.Student(
                name=name, math_score=math, literate_score=literate, english_score=english)

            if student.is_valid():
                student.save()
                print('--- Add successfully ---')
                show_list(models.Student.all())

        elif ans == '2':
            print('type your number')

            print('1: ascending average sort\n'
                  '2: decending average sort\n'
                  )
            sort_ans = input('your answer: ')

            if sort_ans == '1':
                show_list(models.Student.ascending_average_sort())

            elif sort_ans == '2':
                show_list(models.Student.decending_average_sort())

            else:
                print('--- wrong input ---')

        elif ans == '3':
            show_list(models.Student.all())

        elif ans == '4':
            break

        else:
            print('--- wrong input ---')
