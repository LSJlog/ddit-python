package day03;

public class Ooptest {
	public static void main(String[] args) {
		Human hum = new Human();
		System.out.println(hum.age);
		System.out.println(hum);
		hum.birth();
		hum.farming("샷건");
		System.out.println(hum.age);
		System.out.println(hum);
	}
}
