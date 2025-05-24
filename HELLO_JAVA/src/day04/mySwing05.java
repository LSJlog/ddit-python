package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Random;

public class mySwing05 extends JFrame {
	JLabel lbl1;
	JLabel lbl2;
	JLabel lbl3;
	JLabel lbl4;
	JLabel lbl5;
	JLabel lbl6;
	
	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					mySwing05 frame = new mySwing05();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public mySwing05() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lbl1 = new JLabel("__");
		lbl1.setBounds(33, 25, 28, 15);
		contentPane.add(lbl1);
		
		lbl2 = new JLabel("__");
		lbl2.setBounds(73, 25, 28, 15);
		contentPane.add(lbl2);
		
		lbl3 = new JLabel("__");
		lbl3.setBounds(113, 25, 28, 15);
		contentPane.add(lbl3);
		
		lbl4 = new JLabel("__");
		lbl4.setBounds(153, 25, 28, 15);
		contentPane.add(lbl4);
		
		lbl5 = new JLabel("__");
		lbl5.setBounds(193, 25, 28, 15);
		contentPane.add(lbl5);
		
		lbl6 = new JLabel("__");
		lbl6.setBounds(233, 25, 28, 15);
		contentPane.add(lbl6);
		
		JButton btn = new JButton("로또 생성하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btn.setBounds(28, 70, 290, 23);
		contentPane.add(btn);
	}
	
	public void myclick() {
		int[] arr = {
			1, 2, 3, 4, 5, 6, 7, 8, 9 ,10,
			11, 12, 13, 14, 15, 16, 17, 18, 19 ,20,
			21, 22, 23, 24, 25, 26, 27, 28, 29 ,30,
			31, 32, 33, 34, 35, 36, 37, 38, 39 ,40,
			41, 42, 43, 44, 45
		};
		
		for (int i = 0; i <= arr.length; i++) {
			int rnd = (int)(Math.random()*45);
			
			int a = arr[rnd];
			int b = arr[0];
			
			arr[0] = a;
			arr[rnd] = b;
			
		}
		
		lbl1.setText(Integer.toString(arr[0]));
		lbl2.setText(Integer.toString(arr[1]));
		lbl3.setText(Integer.toString(arr[2]));
		lbl4.setText(Integer.toString(arr[3]));
		lbl5.setText(Integer.toString(arr[4]));
		lbl6.setText(Integer.toString(arr[5]));
	}
}
