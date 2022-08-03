import java.util.*;
public class hello {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
			TreeMap <Integer,String> map = new TreeMap<>();
			
			map.put(-12,"srini");
			map.put(5,"srini1");
			map.put(1,"srini2");
			map.put(10,"srini3");
			map.put(-1,"srin4i");
			map.put(9,"srini3");
			map.put(-2,"srin4i");
			map.put(6,"srini3");
			map.put(-3,"srin4i");
			System.out.println(map);
//     o/p  {-12=srini, -3=srin4i, -2=srin4i, -1=srin4i, 1=srini2, 5=srini1, 6=srini3, 9=srini3, 10=srini3} 
//     sorted tree #### map because it store in key value pair
    
    
    	HashMap <Integer,String> map = new HashMap<>();
			
	    map.put(-12,"srini");
			map.put(5,"srini1");
			map.put(1,"srini2");
			map.put(10,"srini3");
			map.put(-1,"srin4i");
			map.put(9,"srini3");
			map.put(-2,"srin4i");
			map.put(6,"srini3");
			map.put(-3,"srin4i");
			
			System.out.println(map);
			
//     o/p {-1=srin4i, 1=srini2, -2=srin4i, -3=srin4i, 5=srini1, 6=srini3, 9=srini3, 10=srini3, -12=srini}
//     based hash dynamically changes maybes takes abs
    
    
    	LinkedHashMap <Integer,String> map = new LinkedHashMap<>();
			
			map.put(-12,"srini");
			map.put(5,"srini1");
			map.put(1,"srini2");
			map.put(10,"srini3");
			map.put(-1,"srin4i");
			map.put(9,"srini3");
			map.put(-2,"srin4i");
			map.put(6,"srini3");
			map.put(-3,"srin4i");
			System.out.println(map);
			
// 			o/p{-12=srini, 5=srini1, 1=srini2, 10=srini3, -1=srin4i, 9=srini3, -2=srin4i, 6=srini3, -3=srin4i}
//     maintain the insertion order maybe uses a linked list
	}
}
