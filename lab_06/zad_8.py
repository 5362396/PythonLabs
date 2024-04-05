def generate_emails(domain):
    with open('maile.txt', 'w', encoding='utf-8') as mails:
        with open('osoby.txt', 'r', encoding='utf-8') as people:
            lines = people.readlines()
            for line in lines:
                email = line.strip('\n').lower().replace(' ', '.').replace('ą', 'a').replace('ć', 'c').replace('ę', 'e').replace('ł', 'l').replace('ń', 'n').replace('ó', 'o').replace('ś', 's').replace('ź', 'z').replace('ż', 'z') + '@' + domain
                mails.write(line.strip('\n') + ', ' + email + '\n')


generate_emails('student.uwm.edu.pl')
