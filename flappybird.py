TITLE = 'Flappy Bird' # Name in the Window  
# Size of the Window in pixels  
WIDTH = 400  
HEIGHT = 708  

def draw():  
    screen.blit('background', (0, 0))
    bird.draw()
    top_pipe.draw()  
    bottom_pipe.draw() 

    screen.draw.text(
        str(bird.score),
        color='white',
        midtop =(20, 10),
        fontsize=70)

def on_mouse_down():  
    # By default this is the left mouse button
    # bird.y -= 50
    bird.speed = -6.5

def hit_pipe():  
   print("Hit pipe!")
   bird.image = "birddead"
   bird.alive = False

def reset():  
   bird.speed = 1
   bird.center = (75, 350)
   bird.alive = True
   top_pipe.center = (300, 0) 
   bottom_pipe.center = (300, top_pipe.height + gap)

   bird.score = 0 # This will hold the points  
   top_pipe.pair_number = 1 # This is number value pair of pipes that have been passed.  

def on_mouse_down():  
    # By default this is the left mouse button
    # bird.y -= 50
    if bird.alive:
        bird.speed = -6.5

def update():  
    bird.y += bird.speed
    top_pipe.x -= scroll_speed  
    bottom_pipe.x -= scroll_speed 
    
    if top_pipe.right < 0:
        offset = random.randint(150, HEIGHT - 150)
        top_pipe.midbottom = (WIDTH, offset)
        bottom_pipe.midbottom = (WIDTH, offset + top_pipe.height + gap)
        top_pipe.pair_number += 1
    
    bird.speed += gravity
    
    if bird.speed > 0:
        bird.image = "bird1"
    else:
        bird.image = "bird0"

    if bird.y > HEIGHT or bird.y < 0:
        reset()
    
    if bird.colliderect(top_pipe) or bird.colliderect(bottom_pipe):  
        hit_pipe()

    if top_pipe.right < bird.x:   # add these 2 new lines
        bird.score = top_pipe.pair_number
    
    if bird.alive:
        if bird.speed > 0:
            bird.image = "bird1"
        else:
            bird.image = "bird0"



gap = 140  
top_pipe = Actor('top', (300, 0))  
bottom_pipe = Actor('bottom', (300, top_pipe.height + gap))
top_pipe.pair_number = 1 
bird = Actor('bird1', (75, 350))  
bird.speed = 1 # add this new line
scroll_speed = 1
gravity = 0.3
bird.alive = True
bird.score = 0