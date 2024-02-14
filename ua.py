import java.util.Scanner;
import java.util.Arrays;
public class Main {
	public static void main(String[] args) {
	    Scanner scan = new Scanner(System.in);
	    
	    String name, age;
	    double tle,ap,filipino,english,esp,mapeh,science,math,sum,result;
	    System.out.println("Simple Code Develop by Prince Sanel Osorio in Java Language\n\n");
	    System.out.print("WHAT IS YOUR NAME? :");
	    name = scan.nextLine().trim();
	    System.out.print("Grade/Section? :");
	    age = scan.nextLine().trim();
	    System.out.println("\nStudent Info\n\nName: \""+name+"\"\nSection: \""+age+"\"");
	    boolean na = true;
	    System.out.println("\n-----------+----------\n  GRADE CALCULATOR\n\n   NUMBER ONLY\n----------+-----------\n");
	    while (na) {
	        try {
	            System.out.print("GRADE IN TLE: ");
	            tle = scan.nextDouble();
	            System.out.print("GRADE IN AP: ");
	            ap = scan.nextDouble();
	            System.out.print("GRADE IN FILIPINO: ");
	            filipino = scan.nextDouble();
	            System.out.print("GRADE IN ENGLISH: ");
	            english = scan.nextDouble();
	            System.out.print("GRADE IN ESP: ");
	            esp = scan.nextDouble();
	            System.out.print("GRADE IN MAPEH: ");
	            mapeh = scan.nextDouble();
	            System.out.print("GRADE IN SCIENCE: ");
	            science = scan.nextDouble();
	            System.out.print("GRADE IN MATH: ");
	            math = scan.nextDouble();
	            sum = tle+ap+filipino+english+esp+mapeh+science+math;
	            result = sum/8;
	            System.out.println("\n\nFINAL GRADE: "+result+"\nThank u.");
	            break;
	      } catch (Exception e){
	        System.out.println("PLEASE USE AN INTEGER NOT NON INTEGER.");
	        scan.nextLine();
	     }
	  }
	    scan.close();
	}
}
