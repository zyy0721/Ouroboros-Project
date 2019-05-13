package com.zyy.llvmIR.Output.com.zyy.llvmIR;

import com.zyy.llvmIR.LLVMLexer;
import com.zyy.llvmIR.LLVMParser;
import com.zyy.llvmIR.LLVMParserBaseListener;
import com.zyy.llvmIR.LLVMParserBaseVisitor;

import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.ANTLRInputStream;
import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.tree.ParseTreeWalker;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class Main {
    public static void run(String expr) throws Exception{
        //对每一个输入的字符串，构造一个 ANTLRStringStream 流 in
        ANTLRInputStream in = new ANTLRInputStream(expr);
        //用 in 构造词法分析器 lexer，词法分析的作用是产生记号
        LLVMLexer lexer = new LLVMLexer(in);
        //用词法分析器 lexer 构造一个记号流 tokens
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        //再使用 tokens 构造语法分析器 parser,至此已经完成词法分析和语法分析的准备工作
        LLVMParser parser = new LLVMParser(tokens);
        //最终调用语法分析器的规则 prog，完成对表达式的验证

        //System.out.println(parser.optPrefix());
        ParseTree tree = parser.module();
        System.out.println("LISP: ");
        System.out.println(tree.toStringTree(parser));
        System.out.println();
        //String name = parser.getSerializedATN();
        //System.out.println("~~~~~grammar File name is " + name);



        System.out.println("Visitor: ");
        LLVMParserBaseVisitor vt = new LLVMParserBaseVisitor();
        vt.visit(tree);
        System.out.println();

        System.out.println("Listener: ");
        ParseTreeWalker walker = new ParseTreeWalker();
        LLVMParserBaseListener lt = new LLVMParserBaseListener();
        walker.walk(lt,tree);
        System.out.println();


       // parser.prog();
    }

    public static void main(String[] args) throws Exception{
        String fileName = "/usr/local/IDEA/llvm/src/com/zyy/llvmIR/Output/com/zyy/llvmIR/test.ll";
        File file = new File(fileName);
        BufferedReader reader = null;
        try{
            reader = new BufferedReader(new FileReader(file));
            String tmpString = null;
            while((tmpString = reader.readLine()) != null){
                run(tmpString);
            }
            reader.close();
        }catch (IOException e){
            e.printStackTrace();
        }finally {
            if(reader != null){
                try{
                    reader.close();
                }catch (IOException e1){

                }
            }
        }
        System.out.println("Hello World");
    }
}