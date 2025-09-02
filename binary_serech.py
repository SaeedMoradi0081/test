def BinarySerech(List:list,Target:int,Low:int,High:int):
    """

    """

    if(Low<=High):
        Mid = (High + Low)//2
        if(List[Mid]==Target):
            return List[Mid]
        elif(List[Mid]<Target):
            return BinarySerech(List,Target,Mid+1,High)
        else:
            return BinarySerech(List,Target,Low,Mid-1)   
    else:
        return "x not in list :)" 
        



numbers = [ -98,-55,-33,0,2,8,10,22,100]
x=999

print(BinarySerech(numbers,x,0,len(numbers)-1))
