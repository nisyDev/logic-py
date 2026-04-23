class Channel:
    def __init__(self, name, desc, subs):
        self.name = name
        self.desc = desc
        self.subs = subs
        self.videos = []

    def subscribe(self, quantity=1):
        self.subs += quantity

    def post(self, video):
        self.videos.append(video)

channel_lancode = Channel('Lan Code', 'Códigos e Gatos', 34000)
channel_guanabara = Channel('Curso e Vídeo', 'Paixão por ensinar', 25000)

class EnterpriseChannel(Channel): #mesmo que seja uma classe Herdeira, temos que construir novamente para definir subclasses exclusivas dessa Class
    def __init__(self, name, desc, subs):
        super().__init__(name, desc, subs) #super é a classe Channel
        self._team = [] #não deve ser manipulado fora da classe
        #só esse canal vai ter equipe, pois mais de uma pessoa irá gerenciar

    @property #para não ficar colocando () ao encapsular. Ex.: print(channel_duolingo.team()) (isso, sem property, com property não precisa)
    def team(self):
        return self._team
    
    def add_employee_team(self, employee):
        if employee not in self._team:
            self._team.append(employee)
        else:
            print(f"{employee} já está na equipe!")
    
    def remove_employee_team(self, employee):
        if employee in self._team:
            self._team.remove(employee)
        else:
            print(f"{employee} não está mais na equipe!")


class Video:
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc

        self.views = 0
        self.likes = 0
        self.dislikes = 0
        self.comments = []

    def watched(self):
        self.views += 1
    
    def liked(self):
        self.likes += 1
    
    def disliked(self):
        self.dislikes += 1

    def commentary(self, commentary):
        self.comments.append(commentary)

    def info(self):
        print(f"""Título: {self.title}
    Descrição: {self.desc}
    {self.views} Visualizações
    {self.likes} Likes {self.dislikes} Deslikes
    {self.comments}\n""")
    
        
video_poo = Video('Python Objects', 'Aprenda Agora!')
video_poo.info()

#composição
#quando coloca uma classe como propriedade de outra

channel_lancode.post(video_poo)