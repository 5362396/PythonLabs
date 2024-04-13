import unidecode


def generate_emails(domain):
    with open('maile.txt', 'w', encoding='utf-8') as mails:
        with open('osoby.txt', 'r', encoding='utf-8') as people:
            lines = people.readlines()
            for line in lines:
                email = unidecode.unidecode(line.strip('\n').lower().replace(' ', '.')) + '@' + domain
                mails.write(line.strip('\n') + ', ' + email + '\n')


generate_emails('student.uwm.edu.pl')
