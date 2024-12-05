import pygame

class Info:
    def __init__(self, place):
        #blits info onto screen corresponding to the image displayed
        self.font = pygame.font.Font(None, 30)
        self.place = place
        self.text = self.get_text(place)
        self.border = 20
        
    def get_text(self, place):
        info_dict = {
            "Hinman": "Hinman community has been home for on campus students for over 50 years. Hinman community has its own convenience store, a ground turf, the Hinman success center and one of the most popular food options called Noodle House. Noodle House serves stir fried noodles with vegetables, meat (or tofu if you're vegan), and a variety of sauces to choose from. Hinman is also the closest community to all of the academic buildings.",
            
            "Dickinson": "One of the newer communities built on campus, has its own soccer field, volleyball area and swing set.",
            
            "Newing": "The second oldest community on campus, this place has been recently renovated which has given students a new turf field, id scanner doors for dorms, and improved study rooms.",
            
            "C4": "Chenango Champlain Collegiate center or also known as C4, a very simple dining hall that offers a good variety of food and drinks, has a Kosher Korner, and continues to serve after 8PM up until 1AM (Called Nite Owl).",
            
            "Mountain View": "A community that gives you a room-with-a-view, has its own tennis, basketball and volleyball courts and a great dining hall.",
            
            "CIW": "College-In-The-Woods has five residence halls: Cayuga, Mohawk, Oneida, Onondaga and Seneca. CIW has an excellent dining hall with the best barbecue on campus, a vegan station, and great breakfast items. It is also host to some fantastic traditions such as Casino-in-the-Woods, where the dining hall is turned into a fully functioning, state-licensed casino, and two different music-oriented events in Woods Jam and WoodStock, featuring local bands and artists.",
            
            "West Gym": "This gym hosts the school’s basketball, volleyball, and wrestling competitions. If you take scuba diving through Binghamton University, this is where you will practice your underwater dives. An overall great place to work out or hang out!",
            
            "East Gym": "The east gym has everything you need if you look to exercise when you spend your time on campus. This is also the place you go to when applying for courses in the Outdoor Pursuits section.",
            
            "Old Dickinson": "The oldest community on campus that has now been turned into a general academic department. Here you can find the math department in Whitney Hall and academic advising in Old Champlain hall.",
            
            "Fine Arts": "The Fine Arts building hosts the schools drawing, painting, sculpting, and printmaking classes. It has a wonderful courtyard. It also has its own art gallery, and is home to the school's theatre department."
        }
        
        return info_dict.get(place)
    
    def wraptext(self, text, max_width):
        words = text.split(' ')
        lines = []
        current_line = words[0]
        
        for word in words[1:]:
            cline = current_line + ' ' + word
            if self.font.size(cline)[0] <= max_width:
                current_line = cline
            else:
                lines.append(current_line)
                current_line = word
        
        lines.append(current_line)
        return lines
    
    def display(self, screen):
        #box setup
        box_x = 0
        box_y = 750 - (750 // 4)
        box_width = 800
        box_height = 750 // 4
        
        pygame.draw.rect(screen, 'black', pygame.Rect(box_x, box_y, box_width, box_height))
        
        wrapping_text = self.wraptext(self.text, box_width - 2 * self.border)
        
        offset = box_y + self.border
        for line in wrapping_text:
            text_format = self.font.render(line, True, "azure")
            screen.blit(text_format, (box_x + self.border, offset))
            offset += self.font.get_height()
        pygame.display.update()