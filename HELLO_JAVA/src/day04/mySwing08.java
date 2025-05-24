package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

import javafx.scene.control.Tab;

import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class mySwing08 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	private JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					mySwing08 frame = new mySwing08();
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
	public mySwing08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("단수:");
		lbl.setBounds(29, 33, 57, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(109, 30, 116, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(29, 58, 196, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(29, 91, 196, 160);
		contentPane.add(ta);
	}
	
	public void myclick() {
		
		if(!ta.getText().isEmpty()) {
			ta.setText("");
		}
		
		String dan = tf.getText();
		int idan = Integer.parseInt(dan);
		
		// 내 풀이
//		for (int i = 1; i < 10; i++) {
//			ta.append(idan + " * " + i + " = " + idan*i + "\n");
//		}
		
//		ta.setText("2*1=2\n2*2=4\n");
		
		String txt = "";
		
//		txt += "2*1=2\n";
//		txt += "2*2=4\n";
//		txt += idan+"*"+1+"="+(idan*1)+"\n";
//		txt += idan+"*"+2+"="+(idan*2)+"\n";
		
		for (int i=1; i<=9; i++) {
			txt += idan + "*" + i + "=" + (idan*i) + "\n";
		}
		
		ta.setText(txt);
	}
}
