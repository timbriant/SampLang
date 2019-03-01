// Generated from c:\Users\201410344\Desktop\antlr4py\SampL.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class SampLLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, StringLiteral=8, 
		Identifier=9, WS=10;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "StringLiteral", 
		"Identifier", "StringCharacters", "StringCharacter", "WS"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'output'", "'var'", "','", "'='", "'['", "']'", "'.'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, "StringLiteral", "Identifier", 
		"WS"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public SampLLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "SampL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\fQ\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3"+
		"\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\5\t\63\n\t\3\t\3\t\3\t\5\t"+
		"8\n\t\3\t\5\t;\n\t\3\n\3\n\7\n?\n\n\f\n\16\nB\13\n\3\13\6\13E\n\13\r\13"+
		"\16\13F\3\f\3\f\3\r\6\rL\n\r\r\r\16\rM\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6"+
		"\13\7\r\b\17\t\21\n\23\13\25\2\27\2\31\f\3\2\6\6\2&&C\\aac|\7\2&&\62;"+
		"C\\aac|\4\2$$^^\5\2\13\f\16\17\"\"\2T\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2"+
		"\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2"+
		"\23\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5\"\3\2\2\2\7&\3\2\2\2\t(\3\2\2"+
		"\2\13*\3\2\2\2\r,\3\2\2\2\17.\3\2\2\2\21:\3\2\2\2\23<\3\2\2\2\25D\3\2"+
		"\2\2\27H\3\2\2\2\31K\3\2\2\2\33\34\7q\2\2\34\35\7w\2\2\35\36\7v\2\2\36"+
		"\37\7r\2\2\37 \7w\2\2 !\7v\2\2!\4\3\2\2\2\"#\7x\2\2#$\7c\2\2$%\7t\2\2"+
		"%\6\3\2\2\2&\'\7.\2\2\'\b\3\2\2\2()\7?\2\2)\n\3\2\2\2*+\7]\2\2+\f\3\2"+
		"\2\2,-\7_\2\2-\16\3\2\2\2./\7\60\2\2/\20\3\2\2\2\60\62\7$\2\2\61\63\5"+
		"\25\13\2\62\61\3\2\2\2\62\63\3\2\2\2\63\64\3\2\2\2\64;\7$\2\2\65\67\7"+
		")\2\2\668\5\25\13\2\67\66\3\2\2\2\678\3\2\2\289\3\2\2\29;\7)\2\2:\60\3"+
		"\2\2\2:\65\3\2\2\2;\22\3\2\2\2<@\t\2\2\2=?\t\3\2\2>=\3\2\2\2?B\3\2\2\2"+
		"@>\3\2\2\2@A\3\2\2\2A\24\3\2\2\2B@\3\2\2\2CE\5\27\f\2DC\3\2\2\2EF\3\2"+
		"\2\2FD\3\2\2\2FG\3\2\2\2G\26\3\2\2\2HI\n\4\2\2I\30\3\2\2\2JL\t\5\2\2K"+
		"J\3\2\2\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2NO\3\2\2\2OP\b\r\2\2P\32\3\2\2"+
		"\2\t\2\62\67:@FM\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}