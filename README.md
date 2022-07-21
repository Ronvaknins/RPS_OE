# Play Rock, Paper Sicssors OR Odd or Even (Deep Learning Project)
Requirements:
  Python 3.7.0
  
  in order to install requirements RPS_OE directory and run this command:
  
    pip install -r requirements.txt
    
Operation:
  
  # Playing Rock Paper add "rps" to to your commands
  
  to Collect Data - images of your hand with the right option each time select:
  
  'r' - rock 
  
  'p' - paper 
  
  's' - sicssors
  
  'n' - nothing
    
  'q' - quit
  
  run this command to start collecting images:
    
     python collect_data.py rps
     
   this window will appear, select your option and put your hand in the green frame:
   ![image](https://user-images.githubusercontent.com/48179479/180248066-676ce231-8046-411b-8fd8-abe17a5981ca.png)
  
  next Train the model using this command:
  
     python train.py rps
     
   to start the game run:
   
    python play.py rps
    
    a window will appear , left side is the computer choices, put your selection in the right frame and play
    
      # Odd or Even add "rps" to to your commands
  
  to Collect Data - images of your hand with the right option each time select:
  'e' - Even 
  
  'o' - Odd 
  
  'n' - nothing
  
  'q' - quit
  
  run this command to start collecting images:
    
     python collect_data.py oe
     
   this window will appear, select your option and put your hand in the green frame:
  ![image](https://user-images.githubusercontent.com/48179479/180250021-045b7bd2-b4ad-401b-849b-8541fc8dc05c.png)

  
  next Train the model using this command:
  
     python train.py oe
     
   to start the game run:
   
    python play.py oe
    
   first select if you are odd or even (click 'e' or 'o' and then enter)
   a window will appear , left side is the computer choices, put your selection in the right frame and play
    
    
   
   
  
