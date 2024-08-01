int dias = Integer.parseInt(txtDias.getText());
        double km = Double.parseDouble(txtKm.getText());
        
        double tarifa = 0.0;
        if(rbPequeño.isSelected()) tarifa = 15;
        if(rbMediano.isSelected()) tarifa = 20;
        if(rbGrande.isSelected()) tarifa = 30;
        
        double costo=0.0;
        if(rbPequeño.isSelected()) tarifa = 0.2*km;
        if(rbMediano.isSelected()) tarifa = 0.3*km;
        if(rbGrande.isSelected()) tarifa = 0.4*km;
        
        double monto=(tarifa*dias)+costo;
        
        double aumento=0;
        if(km>10){
            aumento = monto*(25/100.0);
        }
        monto+=aumento;
        
        txtR.SetText("");
        txtR.append("La cantidad de dias es: "+dias);
        txtR.append("\nLa tarifa asignada es: $"
                + String.format("%.2f", tarifa));
        txtR.append("\nEl costo por kilometro es: $"
                + String.format("%.2f", costo));
        txtR.append("\nEl monto a pagar es: $"
                + String.format("%.2f", monto));