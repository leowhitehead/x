func 𝕩(✗){
    if(✗<=1)
        return ✗;
    return 𝕩(✗-1,)+𝕩(✗-2,);
}

func x(){
    let 🗙 = х("Enter a number: :",);
    X(𝕩(🗙,),);
    X("\n",);
}