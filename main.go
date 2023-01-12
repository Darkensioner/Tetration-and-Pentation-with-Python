//this is a repo for training purposes, i liked go
package main
import "fmt"

//creating a function to power numbers
//since i'm learning, i didn't knew that i needed to say what i wanted to return after receiving the arguments
func power(num1 int, num2 int) (total int){
  total = num1
  // go doesnt have a while loop 🤯
  for counter:=1; counter<num2; counter++ {
    total = num1*total
  }
  return
}


//just copypaste and change powder to tetration and the operation changed from multiplication to power
func tetration(num1 int, num2 int) (total int){
  total = num1
  for counter:=1; counter<num2; counter++ {
    total = power(num1,total)
  }
  return
}

//just copypaste and change tetration to pentation and the operation changed from power to tetration
func pentation(num1 int, num2 int) (total int){
  total = num1
  for counter:=1; counter<num2; counter++ {
    total = tetration(num1,total)
  }
  return
}

//just used an example hello world to know that the program is working
func main() {
  fmt.Println("Hello, world!")
  total := tetration(3, 3)
  fmt.Println(total)
}
