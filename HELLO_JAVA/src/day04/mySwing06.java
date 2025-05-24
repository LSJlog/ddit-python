package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.print.DocFlavor.INPUT_STREAM;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class mySwing06 extends JFrame {

	private JPanel contentPane;
	private JTextField tfMine;
	private JTextField tfCom;
	private JTextField tfResult;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					mySwing06 frame = new mySwing06();
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
	public mySwing06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 473, 239);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblMine = new JLabel("나:");
		lblMine.setBounds(12, 28, 39, 15);
		contentPane.add(lblMine);
		
		JLabel lblCom = new JLabel("컴:");
		lblCom.setBounds(12, 59, 39, 15);
		contentPane.add(lblCom);
		
		JLabel lblResult = new JLabel("결과:");
		lblResult.setBounds(12, 96, 39, 15);
		contentPane.add(lblResult);
		
		tfMine = new JTextField();
		tfMine.setBounds(63, 25, 122, 21);
		contentPane.add(tfMine);
		tfMine.setColumns(10);
		
		tfCom = new JTextField();
		tfCom.setBounds(63, 56, 122, 21);
		tfCom.setColumns(10);
		contentPane.add(tfCom);
		
		tfResult = new JTextField();
		tfResult.setBounds(63, 93, 122, 21);
		tfResult.setColumns(10);
		contentPane.add(tfResult);
		
		JButton btn = new JButton("게임하기");
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
		btn.setBounds(24, 132, 229, 28);
		contentPane.add(btn);
	}
	
	public void myclick() {
		String mine = tfMine.getText();
		String com = "";
		String result = "";
		
		double rnd = Math.random();
		
		if(rnd > 0.5) {
			com = "홀";
		} else {
			com = "짝";
		}
		
		if(mine.equals(com)) {
			result = "승리";
		} else {
			result = "패배";
		}
		
		tfCom.setText(com);
		tfResult.setText(result);
		
	}
}
