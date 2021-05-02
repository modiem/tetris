import styled from 'styled-components';

export const StyledStage = styled.div`
	// width: 100%;
	height: 80vh;
	// max-width: 25vw;
	background: #111;
	display: grid;
	grid-template-rows: repeat(
		${props => props.height}, 1fr);
	grid-template-columns: repeat(
		${props => props.width}, 
		calc( 80vh / ${props => props.height}));
	grid-gap: 1px;
	border: 2px solid #333;
`