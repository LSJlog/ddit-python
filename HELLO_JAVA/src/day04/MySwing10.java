package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing10 extends JFrame {

	private JPanel contentPane;
	private JTextField tfFirst;
	private JTextField tfLast;
	private JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing10 frame = new MySwing10();
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
	public MySwing10() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 600);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tfFirst = new JTextField();
		tfFirst.setBounds(166, 31, 116, 21);
		contentPane.add(tfFirst);
		tfFirst.setColumns(10);
		
		JLabel lblFirst = new JLabel("첫별수:");
		lblFirst.setBounds(40, 34, 57, 15);
		contentPane.add(lblFirst);
		
		JLabel lblLast = new JLabel("끝별수:");
		lblLast.setBounds(40, 79, 57, 15);
		contentPane.add(lblLast);
		
		tfLast = new JTextField();
		tfLast.setColumns(10);
		tfLast.setBounds(166, 76, 116, 21);
		contentPane.add(tfLast);
		
		JButton btn = new JButton("별그리기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(40, 129, 242, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(40, 162, 242, 324);
		contentPane.add(ta);
	}
	
	public String getStar(int cnt) {
		String ret = "";
		for(int i=0; i<cnt; i++) {
			ret += "*";
		}
		ret += "\n";
		return ret;
	}
	
	public void myClick() {
		String first = tfFirst.getText();
		String last = tfLast.getText();
		
		int iFirst = Integer.parseInt(first);
		int iLast = Integer.parseInt(last);
		
		String txt = "";
		
		for(int i=iFirst; i <= iLast; i++) {
			txt += getStar(i);
		}
		ta.setText(txt);
		
		
		
	}
}
