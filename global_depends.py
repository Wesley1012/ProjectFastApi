from fastapi import FastAPI, Depends

def depfunk():
    pass

def depfunk2():
    pass

app = FastAPI(description=[Depends(depfunk), Depends(depfunk2)])

@app.get('/main')
def get_main():
    pass
