package day03;

public class Animal {
	int age = 1;
	
	public void birth() {
		age++;
	}
	
	public static void main(String[] args) {
		Animal ani = new Animal();
		System.out.println(ani.age);
		ani.birth();
		System.out.println(ani.age);
	}
	
}
