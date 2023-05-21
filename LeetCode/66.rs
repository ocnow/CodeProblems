pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
    let mut carry : i32 = 1;
    let digit_len = digits.len();
    let mut result : Vec<i32> = Vec::new();
    for i in (0..digit_len).rev() {
        let mut sum = carry + digits[i];
        if sum > 9 {
            carry = 1;
            sum = 10 - sum;
        }else{
            carry = 0;
        }
        result.insert(0, sum);
    }

    if carry > 0 {
        result.insert(0, carry);
    }
    return result;
}    

fn main(){
   let a = vec![9,9,9]; 
    
   let b = plus_one(a);

   println!("vectore is {:?}",b);
}
