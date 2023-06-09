from website import create_app

app = create_app()

if __name__ =="__main__": #only if we run this file when called not import 
    app.run(debug=True) #start the application and automatically rerun the app
    
    
