package Application Package;

import javax.ejb.Stateless;

/** TODO: generated by FrameWeb. Should be documented. */
@Stateless
public class Pessoa implements Pessoa {
	/** Serialization id (using default value, change if necessary). */
	private static final long serialVersionUID = 1L;
	
	
	
	
	/** TODO: generated by FrameWeb. Should be documented. */
	private String nome;
	
	/** TODO: generated by FrameWeb. Should be documented. */
	private char sexo;
	
	/** TODO: generated by FrameWeb. Should be documented. */
	private password senha;
	

		
	/** Getter for nome. */
	public String getNome() {
		return nome;
	}
	
	/** Setter for nome. */
	public void setNome(String nome) {
		this.nome = nome;
	}
		
	/** Getter for sexo. */
	public char getSexo() {
		return sexo;
	}
	
	/** Setter for sexo. */
	public void setSexo(char sexo) {
		this.sexo = sexo;
	}
		
	/** Getter for senha. */
	public password getSenha() {
		return senha;
	}
	
	/** Setter for senha. */
	public void setSenha(password senha) {
		this.senha = senha;
	}
	
	
	
	/** TODO: generated by FrameWeb. Should be documented. */
	@Override
	public void validarEmail() {
		// FIXME: auto-generated method stub
		return;
	}
	
	/** TODO: generated by FrameWeb. Should be documented. */
	@Override
	public void authenticate() {
		// FIXME: auto-generated method stub
		return;
	}
	
}