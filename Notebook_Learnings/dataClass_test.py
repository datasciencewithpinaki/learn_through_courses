from dataclasses import dataclass

@dataclass
class Investment:
    '''Class that describes investments'''
    
    amt_inr: float = 100
    tenure_years: float = 1.0
    return_pct: float = 0.08

    def get_curr_val(self):
        return self.amt_inr*((1+self.return_pct)**self.tenure_years)

def main():
    myinv = Investment(1e5, 2, 0.1)
    print(myinv)
    curr_val = myinv.get_curr_val()
    return curr_val

if __name__=="__main__":
    curr_val = main()
    print (f'Current Value = INR {curr_val:,.2f}')
