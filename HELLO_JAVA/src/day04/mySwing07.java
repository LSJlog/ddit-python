package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class mySwing07 extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;
	private JTextField tf4;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					mySwing07 frame = new mySwing07();
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
	public mySwing07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf1 = new JTextField();
		tf1.setBounds(24, 26, 59, 21);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		tf2 = new JTextField();
		tf2.setColumns(10);
		tf2.setBounds(125, 26, 59, 21);
		contentPane.add(tf2);
		
		tf3 = new JTextField();
		tf3.setColumns(10);
		tf3.setBounds(24, 68, 59, 21);
		contentPane.add(tf3);
		
		tf4 = new JTextField();
		tf4.setColumns(10);
		tf4.setBounds(242, 68, 59, 21);
		contentPane.add(tf4);
		
		JLabel lbl1 = new JLabel("에서");
		lbl1.setBounds(97, 29, 57, 15);
		contentPane.add(lbl1);
		
		JLabel lbl2 = new JLabel("까지");
		lbl2.setBounds(199, 29, 57, 15);
		contentPane.add(lbl2);
		
		JButton btn = new JButton("배수의 합은");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(95, 67, 135, 23);
		contentPane.add(btn);
	}
	
	public void myclick() {
		String a = tf1.getText();
		String b = tf2.getText();
		String c = tf3.getText();
		
		int aa = Integer.parseInt(a);
		int bb = Integer.parseInt(b);
		int cc = Integer.parseInt(c);
		
		int sum = 0;
		for (int i = aa; i <= bb; i++) {
			if ( i % cc == 0) {
				sum += i;
			}
		}
		
		tf4.setText(Integer.toString(sum));
		
	}
}
