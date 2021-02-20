class BrowserHistory:
    stack = []
    index = 0
    
    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.index = 0

    def visit(self, url: str) -> None:
        if self.stack:
            self.stack = self.stack[:self.index+1] + [url]
            self.index += 1
            
    def back(self, steps: int) -> str:
        if self.index < steps:
            self.index = 0
        else:
            self.index -= steps
        return self.stack[self.index]

    def forward(self, steps: int) -> str:
        if len(self.stack) <= self.index + steps:
            self.index = len(self.stack) - 1
        else:
            self.index += steps
        return self.stack[self.index]



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)