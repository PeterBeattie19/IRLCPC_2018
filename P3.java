import java.util.*;

class Main {
  public static void main(String[] args) {
    LinkedList<Integer> q = new LinkedList<>(); 
    Scanner scan = new Scanner(System.in); 
    
    int n = scan.nextInt(); 
    
    for(int i = n-1; i>=0; i--){
      
      if(i==0){
        q.addFirst(i);
        continue;
      }
        
      
      q.addFirst(i); 
      int p = q.removeLast(); 
      
      q.addFirst(p); 
    }
    
    for(int i: q)
      System.out.print(i +" "); 
  }
}
