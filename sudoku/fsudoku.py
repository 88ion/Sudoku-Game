
import requests
import pygame

pygame.init()
icon=pygame.image.load('icon.png')
window=pygame.display.set_mode((500,600))
pygame.display.set_icon(icon)
window.fill((176,216,230))
pygame.display.set_caption("Sudoku Game")

response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
grid_original = response.json()['board']
grid = [[grid_original[x][y] for y in range(len(grid_original[0]))] for x in range(len(grid_original))]

x=0
y=0
box=500/9

def lines():
    for i in range(0,10):
        if i%3==0 :
            pygame.draw.line(window,(0,0,0),(i*box,0),(i*box,500),6)
            pygame.draw.line(window,(0,0,0),(0,i*box),(500,i*box),6)
        else :
            pygame.draw.line(window,(0,0,0),(i*box,0),(i*box,500),2)
            pygame.draw.line(window,(0,0,0),(0,i*box),(500,i*box),2)

font1 = pygame.font.SysFont("cursive", 35)
font2 = pygame.font.SysFont("verdana", 15)

def isgood(grid,i,j,ans):
    for a in range(0,9):
        
        if grid[a][j]==ans:
            
            return False
            
        if grid[i][a]==ans:
            
            return False
            
        
        x=3*(i//3)+a//3
        
        y=3*(j//3)+a%3
        if grid[x][y]==ans:
            
            return False
            
        
    return True

def highlight():
    for i in range(2):
        pygame.draw.line(window, (0, 160, 0), (x * box-3, (y + i)*box), (x * box + box + 3, (y + i)*box), 4)
        pygame.draw.line(window, (0, 160, 0), ( (x + i)* box, y * box ), ((x + i) * box, y * box + box), 4)

def already():
    for i in range (9):
        for j in range (9):
            if grid[i][j]!= 0:

                pygame.draw.rect(window, (48, 129, 238), (i * box, j * box, box + 1, box + 1))
                text = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                window.blit(text, (i * box + 15, j * box + 15))

def coordinate(pos):
    global x
    x=pos[0]//box
    global y
    y=pos[1]//box

def input(ans):
    text = font1.render(str(ans), 1, (0, 0, 0))
    window.blit(text, (x * box + 15, y * box + 15))

def error2():
    text = font1.render("Please Enter a valid key", 1, (0, 0, 0))
    window.blit(text, (20, 570))

def error1():
    text = font1.render("Eroor", 1, (0, 0, 0))
    window.blit(window, (20, 570))

ans=0
flag=0
flag1=0
out=0
error=0

def instr():
    ftext = font2.render("PRESS D TO RESET / C TO CLEAR", 1, (0, 0, 0))
    stext2 = font2.render("ENTER VALUES AND PRESS ENTER TO VISUALIZE", 1, (0, 0, 0))
    window.blit(ftext, (20, 520))	
    window.blit(stext2, (20, 540))

def output():
    text = font1.render("SUCCESS!! PRESS D or C to continue", 1, (0, 0, 0))
    window.blit(text, (25, 570))

def solve(grid,i,j):
    while grid[i][j]!= 0:
        if i<8:
            i+= 1
        elif i == 8 and j<8:
            i = 0
            j+= 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()
    for k in range(1, 10):
        if isgood(grid, i, j, k)== True:
            grid[i][j]= k
            global x, y
            x = i
            y = j
            window.fill((176,216,230))
            already()
            lines()
            highlight()
            pygame.display.update()
            pygame.time.delay(30)
            if solve(grid, i, j)== 1:
                return True
            else:
                grid[i][j]= 0
            window.fill((176,216,230))

            already()
            lines()
            highlight()
            pygame.display.update()
            pygame.time.delay(20)

    return False


run=True
while run:
    window.fill((176,216,230))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

        if event.type==pygame.MOUSEBUTTONDOWN:
            flag=1
            pos=pygame.mouse.get_pos()
            coordinate(pos)
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                y-=1
                flag=1
            if event.key==pygame.K_DOWN:
                y+=1
                flag=1
            if event.key==pygame.K_LEFT:
                x-=1
                flag=1
            if event.key==pygame.K_RIGHT:
                x+=1
                flag=1
            if event.key==pygame.K_1:
                ans=1
            if event.key==pygame.K_2:
                ans=2
            if event.key==pygame.K_3:
                ans=3
            if event.key==pygame.K_4:
                ans=4
            if event.key==pygame.K_5:
                ans=5
            if event.key==pygame.K_6:
                ans=6
            if event.key==pygame.K_7:
                ans=7
            if event.key==pygame.K_8:
                ans=8
            if event.key==pygame.K_9:
                ans=9
            if event.key==pygame.K_RETURN:
                flag1 = 1
            if event.key==pygame.K_c:
                out = 0
                error = 0
                flag1 = 0
                                
                grid =[
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]

            if event.key == pygame.K_d:
                out = 0
                error = 0
                flag1 = 0
                grid = [[grid_original[x][y] for y in range(len(grid_original[0]))] for x in range(len(grid_original))]

    if flag1==1:
        if solve(grid, 0, 0)== False:
            error = 1
        else:
            out = 1
        flag1 = 0

    if ans!=0:
        input(ans)
        if isgood(grid, int(x), int(y), ans)== True:
            grid[int(x)][int(y)]= ans
            flag = 0
        else:
            grid[int(x)][int(y)]= 0
            error2()
        ans = 0

    if error==1:
        error1()

    if out ==1 :
        output()

    already()
    lines()

    if flag==1:
        highlight()

    instr()

    pygame.display.update()
    
pygame.quit()
          
