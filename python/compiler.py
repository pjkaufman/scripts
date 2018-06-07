import platform
from subprocess import check_output
class CompilerTool:
    #instance variables
    __OS = ''

    #__init__ is the constructor which initializes all instance variables
    def __init__( self ):
        self.__OS = platform.system()
        return None

    #__getOS gets the OS variable
    def __getOS( self ):
        return self.__OS

    #__formatStr takes a string and converts all ','s to either '\\' or '/'
    #param: str is the string to have all commas replaced with either '\\' or '/'
    def __formatStr( self, str ):
        if( self.__getOS() == 'Windows'):
            return str.replace( ',', "\\")    
        else:
            return str.replace( ',', '/')

    #__outputCheck determines whether or not to specify an output location
    #param: start is the beginning of the command to compile the specified files
    #param: cPath is the path to where the file will be compiled to
    #param: outPutFlag is the flag to add to the command in order to specify where to compile the specified files
    def __outputCheck( self, start, cPath, outputFlag ) :
        command = start
        if ( cPath != '' ):
            command += ' ' + outputFlag + ' ' + cPath
        return command

    #__c prepares the command to compile the specified c++ files
    #param: path is the path to where the files that are to be compiled are
    #param: cPath is the path to where the file will be compiled to
    def __c( self, path, cPath ):
        start = 'gcc ' + path
        self.__run( self.__outputCheck( start, cPath, '-o' ))
        return None
    
    #__java prepares the command to compile the specified java files
    #param: path is the path to where the files that are to be compiled are
    #param: cPath is the path to where the file will be compiled to
    def __java( self, path, cPath ):
        start = 'javac -Xlint:unchecked ' + path
        self.__run( self.__outputCheck( start, cPath, '-d' ))
        return None
    
    #__go prepares the command to compile the specified go files
    #param: path is the path to where the files that are to be compiled are
    #param: cPath is the path to where the file will be compiled to
    def __go( self, path, cPath ):
        start = 'go build ' + path
        self.__run( self.__outputCheck( start, cPath, '' ))
        return None

    #__run runs the command that is sent to it
    #param: command is the command to be run
    def __run( self, command ):
        #run the command passed in and determine if an error occurred or not
        try:
            check_output( self.__formatStr( command ), shell=True )
            print 'Compiled files'
        except:
            print 'An error occurred during compilation'
        return None
    
    #compile compiles the specified files and determines where to send the output
    #param: lang is the language specified by the user
    #param: path is the path to where the files that are to be compiled are
    #param: cPath is the path to where the file will be compiled to
    def compile( self, lang, path, cPath ):
        if ( lang == 'c++' ):
            self.__c( path, cPath )
        elif ( lang == 'java' ):
            self.__java( path, cPath )
        elif ( lang == 'go' ):
            self.__go( path, cPath )   
        else:
            print 'Please enter one of the listed language options.'
        
        return None

def main():
    compiler = CompilerTool()
    while True:
        print 'Control+c to exit the program'
        print "Note: all '\\' or '/' should be ','"
        lang = raw_input( 'Enter the type of file to compile (c++, java, or go): ' )
        path = raw_input( 'Enter the path to the files to comipile: ' )
        cPath = rout = raw_input( 'Enter the path to where the compiled files should be stored (leave empty to compile to the same directory): ' )
        compiler.compile( lang, path, cPath )


if  __name__ =='__main__':main()