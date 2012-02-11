from toolbox.pairinggroup import *
from toolbox.PKSig import PKSig
import sys

group = None
debug = None
H = None
bodyKey = 'Body'

def __init__( groupObj ) : 
	global group , debug 
	group= groupObj 
	debug= False 

def getPKdict( mpk , pk , k ) : 
	A_pk , B_pk , C_pk= { } , { } , { } 
	A_pk [ 0 ]= mpk [ k [ 0 ] ] 
	B_pk [ 0 ]= mpk [ k [ 1 ] ] 
	C_pk [ 0 ]= mpk [ k [ 2 ] ] 
	for i in pk.keys( ) : 
		pass
		A_pk [ i ]= pk [ i ] [ k [ 0 ] ] 
		B_pk [ i ]= pk [ i ] [ k [ 1 ] ] 
		C_pk [ i ]= pk [ i ] [ k [ 2 ] ] 
	return A_pk , B_pk , C_pk 

def run_Ind(verifyArgsDict, groupObjParam, verifyFuncArgs):
	global group
	global debug, H
	group = groupObjParam

	N = len(verifyArgsDict)
	z = 0
	At , Bt , Ct= getPKdict( verifyArgsDict[z]['mpk'][bodyKey] , verifyArgsDict[z]['pk'][bodyKey] , [ 'At' , 'Bt' , 'Ct' ] )
	l= len( At.keys( ) )
	incorrectIndices = []
	H = lambda a: group.hash(('1', str(a)), ZR)
	__init__(group)

	for z in range(0, N):
		for arg in verifyFuncArgs:
			if (group.ismember(verifyArgsDict[z][arg][bodyKey]) == False):
				sys.exit("ALERT:  Group membership check failed!!!!\n")

		pass

		if debug : print( "Verifying..." )
		At , Bt , Ct= getPKdict( verifyArgsDict[z]['mpk'][bodyKey] , verifyArgsDict[z]['pk'][bodyKey] , [ 'At' , 'Bt' , 'Ct' ] )
		l= len( At.keys( ) )
		if debug : print( "Length=>" , l )
		D= pair( verifyArgsDict[z]['mpk'][bodyKey][ 'g1' ] , verifyArgsDict[z]['mpk'][bodyKey][ 'g2' ] )
		S , t= verifyArgsDict[z]['sig'][bodyKey][ 'S' ] , verifyArgsDict[z]['sig'][bodyKey][ 't' ]
		m= H( verifyArgsDict[z]['M'][bodyKey] )
		prod_result= 1
		for i in range( l ) :
			pass
			prod_result *= pair( S [ i ] , At [ i ] *( Bt [ i ] ** m ) *( Ct [ i ] ** t [ i ] ) )
		if debug : print( "final result=>" , prod_result )
		if debug : print( "D=>" , D )
		if prod_result== D :
			pass
		else:
			if z not in incorrectIndices:
				incorrectIndices.append(z)

	return incorrectIndices
