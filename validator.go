package dictionary
import "fmt"




func var_hash(args...string){
	type validator_hash struct {}
	for i := 0; i < parser.section().length(); i++ {
		if parser.section() == args {
			validator_hash = parser.section()
		}
	}
	return validator_hash
}

var validator_hash /*type de retour */:= var_hash()

func validator_fail(args...string){
	type validator_fail_count struct {}
	for i := 0; i < parser.section().length(); i++ {
		if parser.section() == args {
			validator_fail_count = 0
		}
	}
	return validator_fail_count
}

var validator_fail_count /*type de retour */:= validator_fail()

curent_height := // nombre de block actuel dans la blockchain

func missed_block(range){
	low_height = current_height - range
	for i = low_height ; i <= current_height ; i++{
		block_signature := //block actuel
		for key, value := range validator_hash {
			if value == false
				validator_fail_count = validator_fail_count + 1
				fmt.println("The block" + block_signature + "has been missed at " + i)
		}
	}
	fmt.println(validator_fail_count)
}
